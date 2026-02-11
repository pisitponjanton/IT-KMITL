error id: file://<WORKSPACE>/hello-world/src/main/scala/Main.scala:`<none>`.
file://<WORKSPACE>/hello-world/src/main/scala/Main.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:
	 -conuter.
	 -conuter#
	 -conuter().
	 -scala/Predef.conuter.
	 -scala/Predef.conuter#
	 -scala/Predef.conuter().
offset: 83
uri: file://<WORKSPACE>/hello-world/src/main/scala/Main.scala
text:
```scala
@main def hello(): Unit =
  var counter  = 0
  def increment(): Unit = 
    conuter@@ += 1

  println(s"Initial counter: $counter")
  increment()
  println(s"Counter after increment: $counter")

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.