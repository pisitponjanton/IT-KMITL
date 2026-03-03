package core

import model.{Record, CleanRecord}
import scala.concurrent.{Future, ExecutionContext}

object ClearData {
// ฟังก์ชันสำหรับแปลง Record ให้เป็น CleanRecord
// โดยจะคัดกรองข้อมูลที่ไม่ถูกต้อง (เช่น id เป็น null หรือว่าง)
// และจัดการความผิดพลาดด้วย Either
//
// - ถ้า id ถูกต้อง (ไม่เป็น null และไม่เป็นค่าว่าง) จะคืนค่า Right(CleanRecord)
// - ถ้า id ไม่ถูกต้อง จะคืนค่า Left พร้อมข้อความ error
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

  // ฟังก์ชันสำหรับแปลง Seq[Record] ให้เป็น Seq[CleanRecord]
  // โดยเรียกใช้ safeTransform กับทุก element ในลิสต์
  // และจะเก็บเฉพาะรายการที่แปลงสำเร็จ (Right)
  // ส่วนรายการที่เกิด error (Left) จะถูกตัดทิ้ง
  def clearSeq(data: Seq[Record]): Seq[CleanRecord] =
    data.map(safeTransform).collect { case Right(clean) =>
      clean
    }

  // ฟังก์ชันสำหรับแปลง Seq[Record] เป็น Seq[CleanRecord] แบบขนาน (parallel)
  // โดยแบ่งข้อมูลออกเป็นหลาย ๆ ชุด (chunk) ตามจำนวน CPU cores
  // แล้วประมวลผลแต่ละชุดพร้อมกันด้วย Future
  //
  // - ใช้ safeTransform ในการตรวจสอบและแปลงข้อมูลแต่ละ Record
  // - เก็บเฉพาะรายการที่แปลงสำเร็จ (Right)
  // - รวมผลลัพธ์จากทุก Future กลับมาเป็น Seq เดียว
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
