import scala.annotation.tailrec

@main def hello(): Unit =
  //def factorial(n: Int, acc: Int = 1): Int = 
  //  if (n <= 1) acc
  //  else factorial(n - 1, acc * n) // Tail Call

  //@tailrec
  //def factorial(n: Int, acc: Int = 1): Int = {
  //  if (n <= 1) acc
  //  else factorial(n - 1, acc * n)
  //}
  
  //@tailrec
  //def factorial(n: Int): Int = {
  //  if (n <= 1) 1
  //  else n * factorial(n - 1) // ไม่ใช่ tail call เพราะมี *n หลังจาก recursive call
  //}

  // DON'T DO THIS!
  def last[A](list: List[A]): A = list match
    case Nil         => throw new Exception("last(empty)")
    case _ :: tail   => last(tail)

  @tailrec
  def last2[A](list: List[A]): A = 
    list match
    case Nil          => throw new Exception("last(empty)")
    case head :: tail => if tail.isEmpty then head else last2(tail)


  def concat[A](list1: List[A], list2: List[A]): List[A] = list1 match
    case Nil            => list2
    case head1 :: tail1 => head1 :: concat(tail1, list2)

  def append[A](list: List[A], value: A): List[A] = list match
    case Nil => value :: Nil
    case head :: tail => head :: append(tail, value)

  def flatten[A](list: List[List[A]]): List[A] = list match
    case Nil          => Nil
    case head :: tail => concat(head, flatten(tail))

  // def group1[A](list: List[A], k: Int): List[List[A]] =
  //   list.take(k) :: group1(list.drop(k), k)

  // def isEmpty[A](list: List[A]): Boolean = list match
  //   case Nil => true
  //   case _   => false

  // def group[A](list: List[A], k: Int): List[List[A]] =
  //   if isEmpty(list) then Nil
  //   else
  //     val (first, more) = list.splitAt(k)
  //     first :: group(more, k)

  // def insertInSorted(x: Int, sorted: List[Int]): List[Int] = sorted match
  //   case Nil           => List(x)
  //   case min :: others =>
  //     if x < min then x :: sorted
  //     else min :: insertInSorted(x, others)

  // def insertSort(list: List[Int]): List[Int] = list match
  //   case Nil    => list
  //   case h :: t => insertInSorted(h, insertSort(t))

  // println(insertSort(List(3,1,4,2)))

