//สำหรับสร้าง movie.csv ที่มีข้อมูลไม่ครบ
import scala.io.Source
import scala.util.{Try, Success, Failure}
import java.io.{File, PrintWriter}

case class Movie(id: Int, title: String, genre: Option[String], rating: Double, year: Int)

object DataGenerator:
  def createDummyCSV(): String = 
    val filename = "movies.csv"
    val content = """id,title,genre,rating,year
      |1, The Matrix, Sci-Fi, 5.0, 1999
      |2, Inception, Sci-Fi, 4.9, 2010
      |3, Broken Movie, , 2.0, 2020       
      |4, Bad Rating, Action, 100, 2021    
      |5, Titanic, Drama, 4.5, 1997
      |6, Avengers, Action, 4.8, 2012
      |7, Short Line, Action              
      |8, Interstellar, Sci-Fi, 4.9, 2014
      """.stripMargin
    val writer = new PrintWriter(new File(filename))
    writer.write(content)
    writer.close()
    filename

//ต่อ
  
@main def runNetflixCSV(): Unit = 
  val csvFile = DataGenerator.createDummyCSV()
  // val csvFile  = "movies.csv"
  println("\n Read File movies.csv ")

  def parseLine(line: String): Option[Movie] = 
    val cols = line.split(",").map(_.trim)

    if (cols.length < 5) return None 

    val movieTry = Try {
      val id = cols(0).toInt
      val title = cols(1)
      val genre = if cols(2).isEmpty then None else Some(cols(2))
      val rating = cols(3).toDouble
      val year = cols(4).toInt
      
      Movie(id, title, genre, rating, year)
    }

    movieTry match
      case Success(m) => Some(m) 
      case Failure(e) => 
        println(s" Skipping Corrupted Data: '$line' (Reason: ${e.getMessage})")
        None

  val source = Source.fromFile(csvFile)
  
  try
    val rawData = source.getLines().drop(1)  
      .toList 
    val validMovies = rawData
      .flatMap(parseLine) 
    println(s"Success read file: ${validMovies.size} from ${rawData.size} line)")
    println("-" * 50)

    val recommendations = validMovies
      .flatMap(m => m.genre.map(g => (m, g))) 
      .filter((m, g) => g == "Action" || g == "Sci-Fi")
      .map { (m, g) =>
        val weight = if m.year > 2010 then 1.2 else 1.0
        val finalScore = m.rating * weight
        (m.title, g, finalScore)
      }
      .sortBy((title, genre, score) => -score)

    println("Netflix Recommendations (Top Picks):")
    recommendations.foreach { (title, genre, score) =>
      println(f" $title%-15s [$genre%-6s] Score: $score%.2f")
    }

  finally
    source.close() 