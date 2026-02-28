package model

case class CleanRecord(
  id: String,
  title: String,
  thumbnail: String,
  slug: String,
  primaryTag: String,
  viewCount: Long,
  isShowComment: String,
  createdAtdatetime: String,
  description: String,
  shareCount: Long,
  commentCount: Long
)