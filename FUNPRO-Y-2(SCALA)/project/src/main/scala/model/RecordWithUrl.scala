package model

// case class สำหรับเก็บข้อมูลข่าวที่เพิ่ม URL แล้ว
// เป็นขั้นตอนหลังจาก CleanRecord
// โดยตัด field ที่ไม่จำเป็นออก และเพิ่ม derived fields (url, url_image)
case class RecordWithUrl(
    id: String, // รหัสข่าว
    title: String, // ชื่อข่าว
    slug: String, // slug สำหรับ URL
    primaryTag: String, // tag หลัก
    viewCount: Long, // จำนวนการเข้าชม
    isShowComment: String, // flag แสดง/ซ่อน comment
    createdAtdatetime: String, // วันที่และเวลาเผยแพร่
    description: String, // คำอธิบายข่าว
    shareCount: Long, // จำนวนการแชร์
    commentCount: Long, // จำนวนคอมเมนต์
    url: String, // URL ข่าวที่สร้างจาก id
    url_image: String // URL รูปภาพที่สร้างจาก thumbnail
)
