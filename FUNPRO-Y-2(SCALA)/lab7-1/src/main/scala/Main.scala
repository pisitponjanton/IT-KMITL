import scala.collection.parallel.immutable._
import scala.collection.parallel.mutable._

object Main extends App {
  val list = (1 to 1000).toList.par
  print(list)
}