error id: file://<WORKSPACE>/src/main/scala/Main.scala:parallel.
file://<WORKSPACE>/src/main/scala/Main.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -scala/collection/parallel/immutable/scala/collection/parallel.
	 -scala/collection/parallel/mutable/scala/collection/parallel.
	 -scala/collection/parallel.
	 -scala/Predef.scala.collection.parallel.
offset: 244
uri: file://<WORKSPACE>/src/main/scala/Main.scala
text:
```scala
import scala.collection.parallel.immutable._
import scala.collection.parallel.mutable._

object Main extends App {
  // val pa = ParArray.tabulate(1000)(x => 2 * x + 1)
  // println(pa.map(x => (x - 1) / 2))

val pv2 = scala.collection.parallel@@.immutable.ParVector.tabulate(1000)(x => x)
println(pv2.filter(_%2 == 0))
}
```


#### Short summary: 

empty definition using pc, found symbol in pc: 