package util

import scala.concurrent.{Future, ExecutionContext}
import scala.concurrent.duration.*
import scala.concurrent.Await

object Timer {

  def measureSeq[A](block: => A): (A, Long) = {
    val start = System.nanoTime()
    val result = block
    val end = System.nanoTime()
    (result, end - start)
  }

  def measureFuture[A](
      futureBlock: => Future[A]
  )(using ec: ExecutionContext): (A, Long) = {

    val start = System.nanoTime()
    val result = Await.result(futureBlock, Duration.Inf)
    val end = System.nanoTime()

    (result, end - start)
  }
}