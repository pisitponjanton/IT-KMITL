error id: file://<WORKSPACE>/src/main/scala/Main.scala:mutable.
file://<WORKSPACE>/src/main/scala/Main.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -scala/collection/parallel/immutable/scala/collection/parallel/mutable.
	 -scala/collection/parallel/mutable/scala/collection/parallel/mutable.
	 -scala/collection/parallel/mutable.
	 -scala/Predef.scala.collection.parallel.mutable.
offset: 84
uri: file://<WORKSPACE>/src/main/scala/Main.scala
text:
```scala
import scala.collection.parallel.immutable._
import scala.collection.parallel.mutabl@@e._

object Main extends App {
  println("Hello, World!")
  val pa = ParArray.tabulate(1000)(x => 2 * x + 1)
}
```


#### Short summary: 

empty definition using pc, found symbol in pc: 