package model

case class RecordWithYearPercent(
  id: String,
  title: String,
  thumbnail: String,
  slug: String,
  primaryTag: String,
  isShowComment: String,
  createdAtdatetime: String,
  description: String,
  shareCount: Long,
  commentCount: Long,
  // --- New Columns ---
  viewCount: Long,
  year: Int,
  totalByYear: Long,
  viewPercent: Double
)