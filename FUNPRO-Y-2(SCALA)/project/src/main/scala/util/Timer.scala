package util

import scala.concurrent.{Future, ExecutionContext}
import scala.concurrent.duration.*
import scala.concurrent.Await

object Timer {

  // ฟังก์ชันสำหรับวัดเวลาการทำงานของโค้ดแบบ synchronous (sequential)
  // รับ block ของโค้ดแบบ call-by-name
  // และคืนค่าเป็น (ผลลัพธ์ของ block, เวลาที่ใช้เป็น nanoseconds)
  def measureSeq[A](block: => A): (A, Long) = {
    val start = System.nanoTime()
    val result = block
    val end = System.nanoTime()
    (result, end - start)
  }

  // ฟังก์ชันสำหรับวัดเวลาการทำงานของโค้ดแบบ asynchronous (Future)
  // โดยจะรอให้ Future ทำงานเสร็จด้วย Await.result
  // และคืนค่าเป็น (ผลลัพธ์, เวลาที่ใช้เป็น nanoseconds)
  def measureFuture[A](
      futureBlock: => Future[A]
  )(using ec: ExecutionContext): (A, Long) = {

    val start = System.nanoTime()
    val result = Await.result(futureBlock, Duration.Inf)
    val end = System.nanoTime()

    (result, end - start)
  }
}
