package core

import model.*
import scala.concurrent.{Future, ExecutionContext}
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import scala.util.Try

object AllTasks {

  // กำหนดรูปแบบ (pattern) สำหรับ parse และ format วันที่–เวลา
  // รูปแบบ "yyyy-MM-dd H:mm" หมายถึง:
  // - yyyy : ปี ค.ศ. 4 หลัก
  // - MM   : เดือน 2 หลัก
  // - dd   : วัน 2 หลัก
  // - H    : ชั่วโมง (0–23) แบบไม่บังคับเลข 2 หลัก
  // - mm   : นาที 2 หลัก
  //
  // ตัวอย่างรูปแบบวันที่ที่รองรับ: "2024-01-15 9:30" หรือ "2024-01-15 14:05"
  private val formatter =
    DateTimeFormatter.ofPattern("yyyy-MM-dd H:mm")

  // ฟังก์ชันสำหรับดึงค่า "ปี" (Year) ออกจาก String วันที่และเวลา
  // โดยจะพยายาม parse ข้อความให้เป็น LocalDateTime ตาม formatter ที่กำหนด
  // หาก parse สำเร็จ จะคืนค่าปี (Int)
  // หากเกิดข้อผิดพลาด เช่น format ไม่ถูกต้อง จะคืนค่า 0 แทน
  private def extractYear(datetime: String): Int =
    Try(LocalDateTime.parse(datetime.trim, formatter).getYear)
      .getOrElse(0)

  // ฟังก์ชันสำหรับแปลง Record ให้เป็น AllTasksRecord
  // โดยรวมทุกขั้นตอนสำคัญไว้ในที่เดียว ได้แก่:
  // 1. คำนวณปีจาก createdAtdatetime
  // 2. คำนวณยอดรวม viewCount ต่อปี
  // 3. คำนวณเปอร์เซ็นต์ viewCount ต่อปี
  // 4. สร้าง URL ข่าว และ URL รูปภาพ
  //
  // หากปีไม่ถูกต้อง หรือไม่พบ total ของปีนั้น
  // จะคืนค่า Left เพื่อป้องกัน error (เช่น หารด้วยศูนย์)
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
            case _               => "Null"
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
  // ฟังก์ชันสำหรับประมวลผลข้อมูลทุกขั้นตอนแบบ sequential
  // โดยรวมการ:
  // 1. คำนวณปีจาก createdAtdatetime
  // 2. รวมยอด viewCount ต่อปี
  // 3. คำนวณเปอร์เซ็นต์ viewCount ต่อปี
  // 4. สร้าง URL และ URL รูปภาพ
  //
  // และคืนค่าเฉพาะรายการที่ผ่านการตรวจสอบ (Right)
  def runSeq(data: Seq[Record]): Seq[AllTasksRecord] = {
    val withYear = data.map(r => (r, extractYear(r.createdAtdatetime)))

    val totalByYear =
      withYear
        .groupBy(_._2)
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

  // ฟังก์ชันสำหรับประมวลผลข้อมูลทุกขั้นตอนแบบขนาน (parallel end-to-end pipeline)
  // โดยรวมการ:
  // 1. คำนวณปีจาก createdAtdatetime
  // 2. รวมยอด viewCount ต่อปี (aggregation แบบ sequential)
  // 3. คำนวณเปอร์เซ็นต์ + สร้าง URL + รวมข้อมูลทั้งหมด
  //    โดยประมวลผลแบบขนานด้วย Future
  //
  // คืนค่าเป็น Future[Seq[AllTasksRecord]]
  // และเก็บเฉพาะรายการที่ผ่านการตรวจสอบ (Right)
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
