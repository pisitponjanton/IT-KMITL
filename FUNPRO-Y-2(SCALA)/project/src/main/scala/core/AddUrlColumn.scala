package core

import model.{Record, RecordWithUrl}
import scala.concurrent.{Future, ExecutionContext}

object AddUrlColumn {
  private def safeTransform(r: Record): Either[String, RecordWithUrl] = {
    Option(r.id) match {
      case Some(id)
        if id.nonEmpty =>
          val url = s"https://www.sanook.com/news/$id"
          val urlImage = 
            if (r.thumbnail.nonEmpty) s"https:${r.thumbnail}"
            else "Null"
          Right(
            RecordWithUrl(
              id = id,
              title = r.title,
              slug = r.slug,
              primaryTag = r.primaryTag,
              viewCount = r.viewCount,
              isShowComment= r.isShowComment,
              createdAtdatetime = r.createdAtdatetime,
              description = r.description,
              shareCount = r.shareCount,
              commentCount = r.commentCount,
              url = url,
              url_image = urlImage
            )
          )
      case _ =>
        Left("Invalid record for URL generation")
    }
  }

  def addSeq(data: Seq[Record]): Seq[RecordWithUrl] = {
    data.map(safeTransform).collect {
      case Right(clean) => clean
    }
  }

  def addParallel(
      data: Seq[Record]
  )(using ec: ExecutionContext): Future[Seq[RecordWithUrl]] = {

    val cores = Runtime.getRuntime.availableProcessors()
    val chunkSize = Math.max(1, data.size / cores)

    val chunks: Seq[Seq[Record]] = data.grouped(chunkSize).toSeq

    val futures: Seq[Future[Seq[RecordWithUrl]]] =
      chunks.map { chunk =>
        Future {
          val processed =
            chunk.flatMap { r =>

              val result = safeTransform(r)

              result match {
                case Right(clean) => Seq(clean)
                case Left(_)      => Seq.empty
              }
            }
          processed
        }
      }

    val combined = Future.sequence(futures)

    combined.map { list =>
      list.flatten
    }
  }
}