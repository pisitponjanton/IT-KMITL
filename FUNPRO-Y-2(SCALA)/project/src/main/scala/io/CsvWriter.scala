package io

import java.io.{File, PrintWriter}

object CsvWriter {

  private def escape(value: String): String =
    if (value.contains(",") || value.contains("\""))
      "\"" + value.replace("\"", "\"\"") + "\""
    else value

  private def toCsvRow(p: Product): String =
    p.productIterator
      .map(_.toString)
      .map(escape)
      .mkString(",")

  private def headerOf(p: Product): String =
    p.productElementNames.mkString(",")

  def writeCsv[T <: Product](folder: String, filename: String, data: Seq[T]): Unit = {

    if (data.isEmpty) return

    val basePath = new File("src/main/resources")
    val outputFolder = new File(basePath, folder)

    if (!outputFolder.exists()) outputFolder.mkdirs()

    val file = new File(outputFolder, filename)

    val writer = new PrintWriter(file)

    try {
      val header = headerOf(data.head)
      val rows   = data.map(toCsvRow)

      (header +: rows).foreach(writer.println)

    } finally {
      writer.close()
    }
  }
}