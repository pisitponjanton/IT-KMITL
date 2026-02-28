import io.*
import model.*
import core.*
import util.*

import scala.concurrent.ExecutionContext.Implicits.global

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

object Main extends App {

  val data: Seq[Record] = DataLoader.load("data.csv")

  println("======================================")
  println(s"Total records loaded: ${data.size}")
  println("======================================\n")

  runBenchmark(
    name = "Clear Data",
    folder = "clearData",
    seqFunc = ClearData.clearSeq,
    parFunc = ClearData.clearParallel,
    data = data
  )

  runBenchmark(
    name = "Add URL Column",
    folder = "addUrlColumn",
    seqFunc = AddUrlColumn.addSeq,
    parFunc = AddUrlColumn.addParallel,
    data = data
  )

  runBenchmark(
    name = "Year Aggregation",
    folder = "yearAggregation",
    seqFunc = YearAggregation.aggregateSeq,
    parFunc = YearAggregation.aggregateParallel,
    data = data
  )
}