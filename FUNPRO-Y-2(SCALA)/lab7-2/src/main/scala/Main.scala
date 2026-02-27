import scala.concurrent._
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.Await
import scala.concurrent.duration._

def aShortRunningTask(): Int =
  Thread.sleep(500)
  42

def longRunningAlgorithm(): Int =
  Thread.sleep(10000)
  42

def slowlyDouble(x: Int, delay: Long): Future[Int] = Future {
  Thread.sleep(delay)
  x * 2
}

@main def hello(): Unit =

  println("Start short task")
  val x = aShortRunningTask()
  println(s"Short task result: $x")

  println("Start async double")
  val f = slowlyDouble(2, 5000)

  val result = Await.result(f, 10.seconds)
  println(s"Async result: $result")