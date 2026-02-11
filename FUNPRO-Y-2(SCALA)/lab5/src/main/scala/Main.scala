import scala.io.Source
import scala.util.{Using, Try, Failure, Success}

@main def hello(): Unit =
  def one():Unit = 
    val data = List("I", "LOVE", "OnePiece", "and", "JujutsuKaisen")
    val numbers = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    def myTail[A](list:List[A]):List[A] = 
      if list.isEmpty then
        throw new Exception("Emptry List")
      else
      list.tail
    def myDrop[A](x:Int, list:List[A]):List[A]=
      list match {
        case Nil => 
          throw new Exception("Emptry List")
        case _ if x <= 0 =>
          list
        case _ :: tail =>
          myDrop(x-1, tail)
      }
    def myDropWhile[A](list: List[A], f: A => Boolean): List[A] = {
      list match {
        case Nil => Nil
        case head :: tail if f(head) =>
          myDropWhile(tail, f)
        case _ =>
          list
      }
    }
    println(myTail(data))
    println(myDrop(2, data))
    println(myDropWhile(numbers, (x: Int) => x < 10))


  case class ExamResult(name: String, subject: String, score: Int)

  // ฟังก์ชันอ่านไฟล์ CSV
  def loadExamData(filename: String): List[ExamResult] = {
    // Using ช่วยจัดการเปิด-ปิดไฟล์ให้อัตโนมัติ (Resource Safety)
    val result: Try[List[ExamResult]] = Using(Source.fromFile(filename)) { source =>
      source.getLines() // ได้ Iterator ของแต่ละบรรทัด
        .drop(1)        // ทิ้ง Header (บรรทัดแรก)
        .map { line =>
          val cols = line.split(",") // แยกด้วย comma
          // สร้าง Object (ระวัง: ข้อมูลจริงอาจต้องมี Error Handling ถ้า CSV พัง)
          ExamResult(cols(0).trim, cols(1).trim, cols(2).trim.toInt)
        }
        .toList // แปลง Iterator เป็น List เก็บไว้ใน Memory
    }

    // จัดการผลลัพธ์ของการอ่านไฟล์ (Try)
    result match {
      case Success(data) => data // ถ้าอ่านสำเร็จ คืนค่า List
      case Failure(exception) => 
        println(s"Error reading file: ${exception.getMessage}")
        List.empty[ExamResult] // ถ้าพัง คืนค่า List ว่าง (หรือจะ throw ต่อก็ได้)
    }
  }

  // Load Data (Impure Part - ทำที่ขอบของโปรแกรม)
  val filename = "src/main/resources/students.csv"
  val examData = loadExamData(filename)

  // println(examData)
  //code here

  def scoreToGPA(score: Int): Double =
    if (score >= 80) 4.0
    else if (score >= 70) 3.0
    else if (score >= 60) 2.0
    else if (score >= 50) 1.0
    else 0.0

  def calculateGPA(data: List[ExamResult]): List[String] = {
    data
      .groupBy(_.name)
      .map { 
        case (name, records) =>
        val gpas = records.map(r => scoreToGPA(r.score))
        val avgGPA = gpas.sum / gpas.size
        (name, avgGPA)
      }
      .toList
      .sortBy(_._2).reverse
      .map { case (name, gpa) =>
        f"$name: $gpa%.2f"
      }
  }

  val result = calculateGPA(examData)
  println("=== GPA Report from src/main/resources/students.csv ===")
  result.foreach(println)









  


