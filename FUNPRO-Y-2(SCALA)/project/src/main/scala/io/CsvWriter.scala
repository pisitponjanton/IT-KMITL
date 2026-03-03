package io

import java.io.{File, PrintWriter}

object CsvWriter {

  // ฟังก์ชันสำหรับ escape ข้อความก่อนนำไปเขียนเป็นไฟล์ CSV
  //
  // หลักการ:
  // - หากค่ามีเครื่องหมาย comma (,) หรือเครื่องหมาย double quote (")
  //   จะต้องครอบข้อความด้วย double quote
  // - หากมี double quote อยู่ภายในข้อความ
  //   ต้องแทนที่ " ด้วย "" (ตามมาตรฐาน CSV)
  //
  // หากไม่มีอักขระพิเศษ จะคืนค่าเดิม
  private def escape(value: String): String =
    if (value.contains(",") || value.contains("\""))
      "\"" + value.replace("\"", "\"\"") + "\""
    else value

  // ฟังก์ชันสำหรับแปลง case class (Product) 1 รายการ
  // ให้เป็นข้อความ 1 แถวในรูปแบบ CSV
  //
  // ขั้นตอน:
  // 1. ใช้ productIterator เพื่อดึงค่าทุก field ของ case class
  // 2. แปลงค่าแต่ละ field เป็น String
  // 3. เรียก escape เพื่อจัดการ comma / double quote
  // 4. รวมทุก field ด้วย "," ให้เป็น 1 บรรทัด
  private def toCsvRow(p: Product): String =
    p.productIterator
      .map(_.toString)
      .map(escape)
      .mkString(",")

  // ฟังก์ชันสำหรับสร้าง header ของไฟล์ CSV
  // จากชื่อ field ของ case class (Product)
  //
  // ใช้ productElementNames เพื่อดึงชื่อ field ตามลำดับ constructor
  // แล้วรวมเป็น String เดียว คั่นด้วย ","
  private def headerOf(p: Product): String =
    p.productElementNames.mkString(",")

  // ฟังก์ชันสำหรับเขียนข้อมูล Seq ของ case class (Product)
  // ออกเป็นไฟล์ CSV แบบ generic
  //
  // คุณสมบัติ:
  // - รองรับ case class ทุกประเภท (T <: Product)
  // - สร้าง header อัตโนมัติจากชื่อ field
  // - สร้างโฟลเดอร์ปลายทางหากยังไม่มี
  // - เขียนข้อมูลลงไฟล์ใน src/main/resources/{folder}/{filename}
  def writeCsv[T <: Product](
      folder: String,
      filename: String,
      data: Seq[T]
  ): Unit = {

    if (data.isEmpty) return

    val basePath = new File("src/main/resources")
    val outputFolder = new File(basePath, folder)

    if (!outputFolder.exists()) outputFolder.mkdirs()

    val file = new File(outputFolder, filename)

    val writer = new PrintWriter(file)

    try {
      val header = headerOf(data.head)
      val rows = data.map(toCsvRow)

      (header +: rows).foreach(writer.println)

    } finally {
      writer.close()
    }
  }
}
