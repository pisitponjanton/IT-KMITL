import scala.util.Random

@main def hello(): Unit =
  val x: Int = Random.between(1, 4)

  println(s"โปรแกรมออก: ${x match
    case 1 => "ค้อน"
    case 2 => "กรรไกร"
    case 3 => "กระดาษ"
  }")

  //นายพิสิษฐ์ภณ จันทร 67070119
  //นายภาษาณฑ์ ศิวธนเณศ 67070133
  //นายชวเลิศ สาวิตรตระกูล 67070216
  def game(y: Int): String =
    (y, x) match
      case (a, b) if a == b => "draw"
      case (1, 3)           => "lose"
      case (2, 1)           => "lose"
      case (3, 2)           => "lose"
      case _                => "win"

  println(s"ค้อน: ${game(1)}")
  println(s"กรรไกร: ${game(2)}")
  println(s"กระดาษ: ${game(3)}")

