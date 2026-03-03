package core

import model.{Record, RecordWithUrl}
import scala.concurrent.{Future, ExecutionContext}

object AddUrlColumn {
  // ฟังก์ชันสำหรับแปลง Record ให้เป็น RecordWithUrl
  // โดยจะตรวจสอบความถูกต้องของ id ก่อน
  // และสร้าง URL ของข่าว รวมถึง URL ของรูปภาพเพิ่มเติม
  //
  // - ถ้า id ถูกต้อง (ไม่เป็น null และไม่ว่าง) จะคืนค่า Right(RecordWithUrl)
  // - ถ้า id ไม่ถูกต้อง จะคืนค่า Left พร้อมข้อความ error
  private def safeTransform(r: Record): Either[String, RecordWithUrl] = {
    Option(r.id) match {
      case Some(id) if id.nonEmpty =>
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
            isShowComment = r.isShowComment,
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

  // ฟังก์ชันสำหรับแปลง Seq[Record] ให้เป็น Seq[RecordWithUrl]
  // โดยเรียกใช้ safeTransform กับทุก Record
  // และเก็บเฉพาะรายการที่สร้าง URL สำเร็จ (Right)
  // ส่วนรายการที่เกิด error (Left) จะถูกตัดทิ้ง
  def addSeq(data: Seq[Record]): Seq[RecordWithUrl] = {
    data.map(safeTransform).collect { case Right(clean) =>
      clean
    }
  }

  // ฟังก์ชันสำหรับแปลง Seq[Record] ให้เป็น Seq[RecordWithUrl] แบบขนาน (parallel)
  // โดยแบ่งข้อมูลออกเป็นหลาย ๆ ชุดตามจำนวน CPU cores
  // แล้วประมวลผลแต่ละชุดพร้อมกันด้วย Future
  //
  // - ใช้ safeTransform เพื่อสร้าง RecordWithUrl
  // - เก็บเฉพาะรายการที่แปลงสำเร็จ (Right)
  // - รวมผลลัพธ์จากทุก Future ให้เป็น Seq เดียว
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
