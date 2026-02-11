import java.time.DayOfWeek

@main def hello(): Unit =
  def addToTotal(currentTotal: Int, n: Int): Int = currentTotal + n
  
  // val start = 0
  // val step1 = addToTotal(start, 5)
  // val step2 = addToTotal(step1, 10)
  // println(s"Current total: ${step2}")

  def checkGrade(score: Int): String = 
    if(score >= 50) then
      s"Congratulations! You passed."
    else
      s"Sorry, you failed. Try again."

  // val result = checkGrade(75)
  // println(result) // Print เพื่อตรวจสอบผลลัพธ์ 


  def normalizeNames(names: List[String]): List[String] =
    names.map { name =>
      name.trim.toLowerCase.capitalize
    }


  // // Test Case
  // val users = List("  somCHAI ", " maNEe  ")
  // val cleanUsers = normalizeNames(users)

  // println(users)      // Expected: List("  somCHAI ", " maNEe  ") (เหมือนเดิม)
  // println(cleanUsers) // Expected: List("Somchai", "Manee") (ของใหม่)


  // Refactor ให้เป็น Pure
  def getDiscountPrice(price: Double, day: DayOfWeek): Double =
    if day == DayOfWeek.MONDAY then
      price * 0.5
    else
      price

  // Test Case
  println(getDiscountPrice(100.0, DayOfWeek.MONDAY))  // Expected: 50.0
  println(getDiscountPrice(100.0, DayOfWeek.FRIDAY))  // Expected: 100.0




