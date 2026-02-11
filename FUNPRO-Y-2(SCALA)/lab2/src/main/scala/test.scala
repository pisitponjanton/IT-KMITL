@main def test(): Unit =
  def func1(x: Int): Int = {
    if (x <= 1) {
      1
    } else {
      val result = func1(x - 1) + func1(x - 2)
      result
    }
  }

  println(func1(1000))
