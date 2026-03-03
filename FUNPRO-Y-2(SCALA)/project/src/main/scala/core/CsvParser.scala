package core

import model.Record

object CsvParser {

  // ฟังก์ชันสำหรับแยกข้อมูล 1 บรรทัดของไฟล์ TSV (Tab-Separated Values)
  // โดยใช้ตัวคั่นเป็นเครื่องหมาย Tab ("\t")
  // และกำหนด limit = -1 เพื่อให้คงค่าช่องว่างท้ายบรรทัดไว้ด้วย
  //
  // คืนค่าเป็น List[String] ของแต่ละ column
  private def splitTsv(line: String): List[String] =
    line.split("\t", -1).toList

  // ฟังก์ชันสำหรับแปลงข้อมูล 1 บรรทัดของไฟล์ TSV
  // ให้เป็น Option[Record]
  //
  // ขั้นตอนการทำงาน:
  // 1. แยก column ด้วย splitTsv
  // 2. ตรวจสอบจำนวน field ให้ตรงกับ schema ที่กำหนด
  // 3. แปลงค่าที่เป็นตัวเลขด้วย toLongOption (ป้องกัน exception)
  // 4. หากโครงสร้างถูกต้อง คืนค่า Some(Record)
  // 5. หากจำนวน field ไม่ตรง คืนค่า None
  def parse(line: String): Option[Record] = {

    splitTsv(line) match {

      case List(
            id,
            title,
            tpe,
            thumbnail,
            slug,
            channel,
            channelOriginal,
            primaryCategory,
            primaryTag,
            viewCount,
            redirectTo,
            isShowComment,
            redirectInternal,
            decors,
            createdAt,
            createdAtdatetime,
            typename,
            description,
            shareCount,
            commentCount,
            gallery
          ) =>
        Some(
          Record(
            id,
            title,
            tpe,
            thumbnail,
            slug,
            channel,
            channelOriginal,
            primaryCategory,
            primaryTag,
            viewCount.toLongOption.getOrElse(0L),
            redirectTo,
            isShowComment,
            redirectInternal,
            decors,
            createdAt,
            createdAtdatetime,
            typename,
            description,
            shareCount.toLongOption.getOrElse(0L),
            commentCount.toLongOption.getOrElse(0L),
            gallery
          )
        )

      case _ => None
    }
  }
}
