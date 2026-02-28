package model

case class Record(
  id: String,
  title: String,
  `type`: String,
  thumbnail: String,
  slug: String,
  channel: String,
  channelOriginal: String,
  primaryCategory: String,
  primaryTag: String,
  viewCount: Long,
  redirectTo: String,
  isShowComment: String,
  redirectInternal: String,
  decors: String,
  createdAt: String,
  createdAtdatetime: String,
  __typename: String,
  description: String,
  shareCount: Long,
  commentCount: Long,
  gallery: String
)