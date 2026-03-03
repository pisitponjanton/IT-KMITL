package model

// case class สำหรับเก็บข้อมูลข่าวที่ผ่านการคัดกรอง (cleaned data)
// โดยตัด field ที่ไม่จำเป็นออก และเก็บเฉพาะข้อมูลหลักที่ใช้ประมวลผลต่อ
case class CleanRecord(
    id: String, // รหัสข่าว
    title: String, // ชื่อข่าว
    thumbnail: String, // path รูปภาพ
    slug: String, // slug สำหรับ URL
    primaryTag: String, // tag หลักของข่าว
    viewCount: Long, // จำนวนการเข้าชม
    isShowComment: String, // flag แสดง/ซ่อน comment
    createdAtdatetime: String, // วันที่และเวลาเผยแพร่
    description: String, // คำอธิบายข่าว
    shareCount: Long, // จำนวนการแชร์
    commentCount: Long // จำนวนคอมเมนต์
)
