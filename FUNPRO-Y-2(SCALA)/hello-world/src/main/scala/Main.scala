@main def functionalExample(): Unit =
  def increment(counter: Int): Int = 
    counter + 1

  val initialCounter = 0 
  val updatedCounter = increment(initialCounter)

  println(s"Initial counter: $initialCounter")
  println(s"Counter after increment: $updatedCounter")
