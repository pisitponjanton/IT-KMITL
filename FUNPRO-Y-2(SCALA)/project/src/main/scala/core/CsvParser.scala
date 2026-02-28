package core

import model.Record

object CsvParser {

  private def splitTsv(line: String): List[String] =
    line.split("\t", -1).toList

  def parse(line: String): Option[Record] = {

    splitTsv(line) match {

      case List(
        id,
        title,
        tpe,
        thumbnail,
        slug,
        channel,
        channelOriginal,
        primaryCategory,
        primaryTag,
        viewCount,
        redirectTo,
        isShowComment,
        redirectInternal,
        decors,
        createdAt,
        createdAtdatetime,
        typename,
        description,
        shareCount,
        commentCount,
        gallery
      ) =>
        Some(
          Record(
            id,
            title,
            tpe,
            thumbnail,
            slug,
            channel,
            channelOriginal,
            primaryCategory,
            primaryTag,
            viewCount.toLongOption.getOrElse(0L),
            redirectTo,
            isShowComment,
            redirectInternal,
            decors,
            createdAt,
            createdAtdatetime,
            typename,
            description,
            shareCount.toLongOption.getOrElse(0L),
            commentCount.toLongOption.getOrElse(0L),
            gallery
          )
        )

      case _ => None
    }
  }
}