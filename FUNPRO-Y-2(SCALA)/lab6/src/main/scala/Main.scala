// import scala.util.{Try, Success, Failure}

// @main def hello(): Unit =
//   def search_0[A](values: List[A], target: A): Int =  // returns -1 when not found
//     values.indexOf(target)

//   def between_0[A](values: List[A], from: A, to: A): List[A] =
//     val i = search_0(values, from)
//     val j = search_0(values, to)
//     values.slice(i min j, (i max j) + 1)  

//   val words = List("one", "two", "three", "four")
//   // println(between_0(words, "two", "four"))
//   // println(between_0(words, "four", "two"))


//   def search_OP[A](values: List[A], target: A): Option[Int] =  
//   Some(values.indexOf(target))

//   def between[A](values: List[A], from: A, to: A): List[A] =
//     (search_OP(values, from), search_OP(values, to)) match
//         case (Some(i), Some(j))   => values.slice(i min j, (i max j) + 1)
//         case _ => List.empty

//   // println(between(words, "two", "five"))
//   // println(between(words, "zero", "four"))

//   def mean_0(xs: Seq[Double], onEmpty: Double): Double =
//   if xs.isEmpty then onEmpty
//   else xs.sum / xs.length

//   // println(mean_0(Seq(1,2,3), 1))
//   // println(mean_0(Seq(), 1) )

//   def mean_1(xs: Seq[Double]): Double =     
//     if xs.isEmpty then
//       throw new ArithmeticException("mean of empty list!")
//     else xs.sum / xs.length        

//   // println(mean_1(Seq(1,2,3)))
//   // println(mean_1(Seq()))

//   def mean(xs: Seq[Double]): Option[Double] =
//     if xs.isEmpty then None
//     else Some(xs.sum / xs.length)

//   // println(mean(Seq(1,2,3)))
//   // println(mean(Seq()))

//   // ------------------------------------------ 2 ------------------------------------------//

//   enum Either[+E, +A]:
//     case Left(value: E)
//     case Right(value: A)

//   import Either.{Left, Right}
  
//   def mean_E(xs: Seq[Double]): Either[String, Double] =
//     if xs.isEmpty then
//       Left("mean of empty list!")
//     else
//       Right(xs.sum / xs.length)

//   println(mean_E(Seq(1,2,3)))
//   println(mean_E(Seq()))




//   // ------------------------------------------ 3 ------------------------------------------//
//   def safeDivideTry(numerator: Int, denominator: Int): Try[Int] =
//     Try {
//       numerator / denominator
//     }

//   // val result1 = safeDivideTry(10, 2)
//   // val result2 = safeDivideTry(10, 0)

//   // result1 match
//   //   case Success(value) =>
//   //     println(s"Result is: $value")

//   //   case Failure(ex) =>
//   //     println(s"Error: ${ex.getMessage}")

//   // result2 match
//   //   case Success(value) =>
//   //     println(s"Result is: $value")

//   //   case Failure(ex) =>
//   //     println(s"Error: ${ex.getMessage}")

    
//   def safeDivideEither(numerator: Int, denominator: Int): Either[String, Int] =
//     if denominator == 0 then
//       Left("Error: Division by zero")
//     else
//       Right(numerator / denominator)

//   val result1 = safeDivideEither(10, 2)
//   val result2 = safeDivideEither(10, 0)

//   result1 match
//   case Right(value) =>
//     println(s"Result is: $value")

//   case Left(errorMessage) =>
//     println(errorMessage)

//   result2 match
//   case Right(value) =>
//     println(s"Result is: $value")

//   case Left(errorMessage) =>
//     println(errorMessage)



// def safeStringToIntOption(input: String): Option[Int] =
//   if input == null || input.isEmpty then
//     None
//   else
//     try
//       Some(input.toInt)
//     catch
//       case _: NumberFormatException => None

// @main def testOption(): Unit =
//   println(safeStringToIntOption("123"))
//   println(safeStringToIntOption("ABC"))
//   println(safeStringToIntOption("")) 


def safeStringToIntEither(input: String): Either[String, Int] =
  if input == null || input.isEmpty then
    Left("Error: Input is empty")
  else
    try
      Right(input.toInt)
    catch
      case _: NumberFormatException =>
        Left("Error: Input is not a valid integer")


@main def testEither(): Unit =
  println(safeStringToIntEither("123"))
  println(safeStringToIntEither("ABC"))
  println(safeStringToIntEither(""))




    

