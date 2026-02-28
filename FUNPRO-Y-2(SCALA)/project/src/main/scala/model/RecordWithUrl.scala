package model

case class RecordWithUrl(
  id: String,
  title: String,
  slug: String,
  primaryTag: String,
  viewCount: Long,
  isShowComment: String,
  createdAtdatetime: String,
  description: String,
  shareCount: Long,
  commentCount: Long,
  url: String,
  url_image: String
)