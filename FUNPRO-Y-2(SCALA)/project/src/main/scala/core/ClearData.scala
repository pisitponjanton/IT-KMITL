package core

import model.{Record, CleanRecord}
import scala.concurrent.{Future, ExecutionContext}

object ClearData {
  private def safeTransform(r: Record): Either[String, CleanRecord] = {

    Option(r.id) match {
      case Some(id) if id.nonEmpty =>
        Right(
          CleanRecord(
            id = id,
            title = r.title,
            thumbnail = r.thumbnail,
            slug = r.slug,
            primaryTag = r.primaryTag,
            viewCount = r.viewCount,
            isShowComment = r.isShowComment,
            createdAtdatetime = r.createdAtdatetime,
            description = r.description,
            shareCount = r.shareCount,
            commentCount = r.commentCount
          )
        )
      case _ =>
        Left(s"Invalid record: ${r.id}")
    }
  }

  def clearSeq(data: Seq[Record]): Seq[CleanRecord] =
    data.map(safeTransform).collect {
      case Right(clean) => clean
    }

  def clearParallel(
      data: Seq[Record]
  )(using ec: ExecutionContext): Future[Seq[CleanRecord]] = {

    val cores = Runtime.getRuntime.availableProcessors()
    val chunkSize = Math.max(1, data.size / cores)

    val chunks: Seq[Seq[Record]] = data.grouped(chunkSize).toSeq

    val futures: Seq[Future[Seq[CleanRecord]]] =
      chunks.map { chunk =>
        Future {
          val cleaned: Seq[CleanRecord] =
            chunk.flatMap { r =>

              val result = safeTransform(r)

              result match {
                case Right(clean) => Seq(clean)
                case Left(_)      => Seq.empty
              }
            }
          cleaned
        }
      }

    val combined: Future[Seq[Seq[CleanRecord]]] = Future.sequence(futures)

    combined.map { listOfSeq =>
      listOfSeq.flatten
    }
  }
}