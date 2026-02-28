package core

import model.{Record, RecordWithYearPercent}
import scala.concurrent.{Future, ExecutionContext}
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import scala.util.Try

object YearAggregation {

  private val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd H:mm")

  private def extractYear(datetime: String): Int =
    Try(LocalDateTime.parse(datetime.trim, formatter).getYear).getOrElse(0)

  private def safeTransform(
      r: Record,
      totalByYear: Map[Int, Long]
  ): Either[String, RecordWithYearPercent] = {

    val year = extractYear(r.createdAtdatetime)

    totalByYear.get(year) match {
      case Some(total) if total > 0 =>
        val percent = (r.viewCount.toDouble / total.toDouble) * 100.0

        val percentRounded =
          BigDecimal(percent)
            .setScale(4, BigDecimal.RoundingMode.HALF_UP)
            .toDouble

        Right(
          RecordWithYearPercent(
            r.id,
            r.title,
            r.thumbnail,
            r.slug,
            r.primaryTag,
            r.isShowComment,
            r.createdAtdatetime,
            r.description,
            r.shareCount,
            r.commentCount,
            r.viewCount,
            year,
            total,
            percentRounded
          )
        )
      case _ =>
        Left("Invalid year or total = 0")
    }
  }

  def aggregateSeq(data: Seq[Record]): Seq[RecordWithYearPercent] = {
    val withYear = data.map(r => (r, extractYear(r.createdAtdatetime)))

    val totalByYear =
      withYear.groupBy(_._2)
      .map { 
        case (year, records) =>
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

  def aggregateParallel(
      data: Seq[Record]
  )(using ec: ExecutionContext): Future[Seq[RecordWithYearPercent]] = {

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
            val result = safeTransform(r, totalByYear)

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