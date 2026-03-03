package model

// case class สำหรับเก็บข้อมูลข่าวดิบ (Raw Data)
// ที่อ่านมาจากไฟล์ TSV/CSV ก่อนผ่านขั้นตอน clean หรือ transform
//
// โมเดลนี้สะท้อนโครงสร้างข้อมูลจากไฟล์ต้นทางแบบครบทุก column
case class Record(
    id: String, // รหัสข่าว
    title: String, // ชื่อข่าว
    `type`: String, // ประเภทของข่าว (ใช้ backtick เพราะเป็น reserved word)
    thumbnail: String, // path รูปภาพ
    slug: String, // slug สำหรับ URL
    channel: String, // ช่องทางเผยแพร่
    channelOriginal: String, // ช่องทางต้นฉบับ
    primaryCategory: String, // หมวดหมู่หลัก
    primaryTag: String, // tag หลัก
    viewCount: Long, // จำนวนการเข้าชม
    redirectTo: String, // URL redirect ภายนอก
    isShowComment: String, // flag แสดง/ซ่อน comment
    redirectInternal: String, // redirect ภายในระบบ
    decors: String, // ข้อมูลตกแต่งเพิ่มเติม
    createdAt: String, // วันที่สร้าง (format ดั้งเดิม)
    createdAtdatetime: String, // วันที่และเวลาแบบละเอียด
    __typename: String, // type name
    description: String, // คำอธิบายข่าว
    shareCount: Long, // จำนวนการแชร์
    commentCount: Long, // จำนวนคอมเมนต์
    gallery: String // ข้อมูลแกลเลอรี
)
