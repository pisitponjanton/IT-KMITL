package model

case class AllTasksRecord(
  id: String,
  title: String,
  slug: String,
  primaryTag: String,
  isShowComment: String,
  createdAtdatetime: String,
  description: String,
  shareCount: Long,
  commentCount: Long,
  viewCount: Long,
  year: Int,
  totalByYear: Long,
  viewPercent: Double,
  url: String,
  url_image: String,
)