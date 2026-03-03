package core

import model.{Record, RecordWithYearPercent}
import scala.concurrent.{Future, ExecutionContext}
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import scala.util.Try

object YearAggregation {

  // กำหนดรูปแบบ (pattern) สำหรับ parse และ format วันที่–เวลา
  // รูปแบบ "yyyy-MM-dd H:mm" หมายถึง:
  // - yyyy : ปี ค.ศ. 4 หลัก
  // - MM   : เดือน 2 หลัก
  // - dd   : วัน 2 หลัก
  // - H    : ชั่วโมง (0–23) แบบไม่บังคับเลข 2 หลัก
  // - mm   : นาที 2 หลัก
  //
  // ตัวอย่างรูปแบบวันที่ที่รองรับ: "2024-01-15 9:30" หรือ "2024-01-15 14:05"
  private val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd H:mm")

  // ฟังก์ชันสำหรับดึงค่า "ปี" (Year) ออกจาก String วันที่และเวลา
  // โดยจะพยายาม parse ข้อความให้เป็น LocalDateTime ตาม formatter ที่กำหนด
  // หาก parse สำเร็จ จะคืนค่าปี (Int)
  // หากเกิดข้อผิดพลาด เช่น format ไม่ถูกต้อง จะคืนค่า 0 แทน
  private def extractYear(datetime: String): Int =
    Try(LocalDateTime.parse(datetime.trim, formatter).getYear).getOrElse(0)

  // ฟังก์ชันสำหรับแปลง Record ให้เป็น RecordWithYearPercent
  // โดยจะคำนวณสัดส่วน (percentage) ของ viewCount เทียบกับยอดรวมของปีนั้น
  //
  // ขั้นตอนการทำงาน:
  // 1. ดึงปีจาก createdAtdatetime ด้วย extractYear
  // 2. ตรวจสอบว่ามียอดรวม (total) ของปีนั้นใน totalByYear และต้องมากกว่า 0
  // 3. คำนวณเปอร์เซ็นต์ viewCount ต่อ total
  // 4. ปัดเศษทศนิยม 4 ตำแหน่ง (HALF_UP)
  // 5. หากข้อมูลถูกต้อง คืนค่า Right(RecordWithYearPercent)
  // 6. หากไม่พบปี หรือ total = 0 คืนค่า Left พร้อมข้อความ error
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

  // ฟังก์ชันสำหรับ aggregate ข้อมูลแบบ sequential
  // โดยคำนวณยอดรวม viewCount ต่อปี
  // และสร้าง RecordWithYearPercent สำหรับแต่ละ Record
  //
  // ขั้นตอน:
  // 1. ดึงปีจาก createdAtdatetime ของแต่ละ Record
  // 2. รวมยอด viewCount แยกตามปี (totalByYear)
  // 3. เรียก safeTransform เพื่อคำนวณเปอร์เซ็นต์รายรายการ
  // 4. เก็บเฉพาะรายการที่แปลงสำเร็จ (Right)
  def aggregateSeq(data: Seq[Record]): Seq[RecordWithYearPercent] = {
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

  // ฟังก์ชันสำหรับ aggregate ข้อมูลแบบขนาน (parallel)
  // โดยคำนวณยอดรวม viewCount ต่อปีแบบ sequential ก่อน
  // แล้วกระจายการคำนวณเปอร์เซ็นต์ของแต่ละ Record ไปทำงานพร้อมกันด้วย Future
  //
  // ขั้นตอนหลัก:
  // 1. ดึงปีจาก createdAtdatetime
  // 2. คำนวณยอดรวม viewCount ต่อปี (totalByYear)
  // 3. แบ่งข้อมูลออกเป็นหลาย chunk ตามจำนวน CPU cores
  // 4. ประมวลผลแต่ละ chunk แบบขนาน
  // 5. รวมผลลัพธ์ทั้งหมดกลับมาเป็น Seq เดียว
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
