package core

import model.*
import scala.concurrent.{Future, ExecutionContext}
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import scala.util.Try

object AllTasks {

  private val formatter =
    DateTimeFormatter.ofPattern("yyyy-MM-dd H:mm")

  private def extractYear(datetime: String): Int =
    Try(LocalDateTime.parse(datetime.trim, formatter).getYear)
      .getOrElse(0)

  private def safeTransform(
      r: Record,
      totalByYear: Map[Int, Long]
  ): Either[String, AllTasksRecord] = {

    val year = extractYear(r.createdAtdatetime)

    totalByYear.get(year) match {
      case Some(total) if total > 0 =>
        val percent = (r.viewCount.toDouble / total.toDouble) * 100.0

        val percentRounded =
          BigDecimal(percent)
            .setScale(4, BigDecimal.RoundingMode.HALF_UP)
            .toDouble

        val url =
            r.id match {
                case t if t.nonEmpty => s"https://www.sanook.com/news/${r.id}"
                case _ => "Null"
            }

        val urlImage =
          r.thumbnail match {
            case t if t.nonEmpty => s"https:$t"
            case _               => "Null"
          }

        Right(
          AllTasksRecord(
            id = r.id,
            title = r.title,
            slug = r.slug,
            primaryTag = r.primaryTag,
            isShowComment = r.isShowComment,
            createdAtdatetime = r.createdAtdatetime,
            description = r.description,
            shareCount = r.shareCount,
            commentCount = r.commentCount,
            viewCount = r.viewCount,
            year = year,
            totalByYear = total,
            viewPercent = percentRounded,
            url = url,
            url_image = urlImage
          )
        )

      case _ =>
        Left("Invalid year or total")
    }
  }

  def runSeq(data: Seq[Record]): Seq[AllTasksRecord] = {
    val withYear = data.map(r => (r, extractYear(r.createdAtdatetime)))

    val totalByYear =
      withYear.groupBy(_._2)
        .map { case (year, records) =>
          year -> records.map(_._1.viewCount).sum
        }

    data.flatMap { r =>
      val result = safeTransform(r, totalByYear)

      result match {
        case Right(valid) => Seq(valid)
        case Left(_)      => Seq.empty
      }
    }
  }

  def runParallel(
      data: Seq[Record]
  )(using ec: ExecutionContext): Future[Seq[AllTasksRecord]] = {

    val cores = Runtime.getRuntime.availableProcessors()
    val chunkSize = Math.max(1, data.size / cores)

    val withYear =
      data.map(r => (r, extractYear(r.createdAtdatetime)))

    val totalByYear =
      withYear
        .groupBy(_._2)
        .map { case (year, records) =>
          year -> records.map(_._1.viewCount).sum
        }

    val chunks =
      data.grouped(chunkSize).toSeq

    val futures =
      chunks.map { chunk =>
        Future {

          chunk.flatMap { r =>

            val result =
              safeTransform(r, totalByYear)

            result match {
              case Right(valid) => Seq(valid)
              case Left(_)      => Seq.empty
            }
          }
        }
      }
    val combined = Future.sequence(futures)

    combined.map { list =>
      list.flatten
    }
  }
}