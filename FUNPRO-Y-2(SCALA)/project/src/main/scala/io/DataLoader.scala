package io

import scala.io.Source
import core.CsvParser
import model.Record

object DataLoader {

  // ฟังก์ชันสำหรับโหลดไฟล์ CSV/TSV จาก resources
  // แล้วแปลงแต่ละบรรทัดให้เป็น Seq[Record]
  //
  // ขั้นตอน:
  // 1. โหลดไฟล์จาก classpath ด้วย getResourceAsStream
  // 2. ข้าม header (บรรทัดแรก)
  // 3. parse แต่ละบรรทัดเป็น Record
  // 4. กรองเฉพาะบรรทัดที่ parse สำเร็จ
  // 5. ปิด resource อย่างปลอดภัย
  def load(filename: String): Seq[Record] = {

    Option(getClass.getClassLoader.getResourceAsStream(filename)) match {

      case Some(stream) =>
        val source = Source.fromInputStream(stream)

        try {
          source
            .getLines()
            .drop(1)
            .toVector
            .flatMap(CsvParser.parse)
        } finally {
          source.close()
        }

      case None =>
        println(s"File not found: $filename")
        Seq.empty
    }
  }
}
