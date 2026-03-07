import io.*
import model.*
import core.*
import util.*

import scala.concurrent.ExecutionContext.Implicits.global

// ฟังก์ชันสำหรับรัน benchmark เปรียบเทียบ
// ระหว่างเวอร์ชัน Sequential และ Parallel
//
// รับ:
// - name     : ชื่อ task สำหรับแสดงผล
// - folder   : โฟลเดอร์สำหรับ export CSV
// - seqFunc  : ฟังก์ชันแบบ sequential
// - parFunc  : ฟังก์ชันแบบ parallel (Future)
// - data     : ข้อมูล input (Seq[Record])
//
// ทำหน้าที่:
// 1. วัดเวลา seqFunc
// 2. วัดเวลา parFunc
// 3. คำนวณ speedup
// 4. แสดงผล benchmark
// 5. export ผลลัพธ์เป็น CSV
def runBenchmark[T <: Product](
    name: String,
    folder: String,
    seqFunc: Seq[Record] => Seq[T],
    parFunc: Seq[Record] => scala.concurrent.Future[Seq[T]],
    data: Seq[Record]
): Unit = {

  val (seqResult, seqTime) =
    Timer.measureSeq {
      seqFunc(data)
    }

  val (parResult, parTime) =
    Timer.measureFuture {
      parFunc(data)
    }

  val speedup =
    if (parTime == 0) 0.0
    else seqTime.toDouble / parTime.toDouble

  println("======================================")
  println(s"Task: $name")
  println("--------------------------------------")
  println(s"Total Records: ${seqResult.size}")
  println(s"Seq time: ${seqTime / 1000000} ms")
  println(s"Parallel time: ${parTime / 1000000} ms")
  println(f"Speedup: $speedup%.4f")
  println("======================================\n")

  CsvWriter.writeCsv(folder, "output_seq.csv", seqResult)
  CsvWriter.writeCsv(folder, "output_parallel.csv", parResult)
}

// Entry point ของโปรแกรม
// ทำหน้าที่:
// 1. โหลดข้อมูลจากไฟล์
// 2. แสดงจำนวน record ที่โหลดได้
// 3. รัน benchmark เปรียบเทียบ Sequential vs Parallel
//    สำหรับแต่ละ task ในระบบ
object Main extends App {

  val data: Seq[Record] = DataLoader.load("data.csv")

  println("======================================")
  println(s"Total records loaded: ${data.size}")
  println("======================================\n")

  // runBenchmark(
  //   name = "Clear Data",
  //   folder = "clearData",
  //   seqFunc = ClearData.clearSeq,
  //   parFunc = ClearData.clearParallel,
  //   data = data
  // )

  // runBenchmark(
  //   name = "Add URL Column",
  //   folder = "addUrlColumn",
  //   seqFunc = AddUrlColumn.addSeq,
  //   parFunc = AddUrlColumn.addParallel,
  //   data = data
  // )

  // runBenchmark(
  //   name = "Year Aggregation",
  //   folder = "yearAggregation",
  //   seqFunc = YearAggregation.aggregateSeq,
  //   parFunc = YearAggregation.aggregateParallel,
  //   data = data
  // )

  runBenchmark(
    name = "All Tasks",
    folder = "allTasks",
    seqFunc = AllTasks.runSeq,
    parFunc = AllTasks.runParallel,
    data = data
  )
}
