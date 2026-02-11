@main def Lab2(): Unit =
  val f:Int => Int = x => x + 1 
  val g:Int => Int = x => x * x

  // println(f(5))
  // println(g(5))

  def applyTwice(h: Int => Int ,x : Int) : Int = {
    h(h(x))
  }
  // println(applyTwice(f,5))
  // println(applyTwice(g,5))

  def myCompose( func1: Int => Int , func2: Int => Int ) : Int => Int ={
    (x : Int) => func1(func2(x))
  }

  val f_of_g = myCompose(f, g)
  // println(f_of_g(5)) 

  val builtInCompose = f.compose(g)  
  val builtInAndThen = f.andThen(g)

  println(builtInCompose(5)) // (5^2) + 1 = 26
  println(builtInAndThen(5)) // (5+1)^2 = 36

