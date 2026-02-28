package io

import scala.io.Source
import core.CsvParser
import model.Record

object DataLoader {

  def load(filename: String): Seq[Record] = {

    Option(getClass.getClassLoader.getResourceAsStream(filename)) match {

      case Some(stream) =>
        val source = Source.fromInputStream(stream)

        try {
          source
            .getLines()
            .drop(1)              
            .toVector                
            .flatMap(CsvParser.parse)
        } finally {
          source.close()
        }

      case None =>
        println(s"File not found: $filename")
        Seq.empty
    }
  }
}