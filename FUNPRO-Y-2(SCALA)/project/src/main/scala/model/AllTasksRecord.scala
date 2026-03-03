package model

// case class สำหรับเก็บข้อมูลผลลัพธ์สุดท้ายของทุกขั้นตอน (All Tasks)
// รวมข้อมูลต้นฉบับ + ข้อมูลที่คำนวณเพิ่ม (derived fields)
//
// ใช้เป็น output model สำหรับ export CSV หรือแสดงผล
case class AllTasksRecord(
    id: String, // รหัสข่าว
    title: String, // ชื่อข่าว
    slug: String, // slug สำหรับ URL
    primaryTag: String, // tag หลักของข่าว
    isShowComment: String, // flag แสดง/ซ่อน comment
    createdAtdatetime: String, // วันที่และเวลาเผยแพร่
    description: String, // คำอธิบายข่าว
    shareCount: Long, // จำนวนการแชร์
    commentCount: Long, // จำนวนคอมเมนต์
    viewCount: Long, // จำนวนการเข้าชม
    year: Int, // ปีที่ดึงมาจาก createdAtdatetime
    totalByYear: Long, // ยอดรวม viewCount ทั้งปีนั้น
    viewPercent: Double, // เปอร์เซ็นต์ view ของข่าวนี้เทียบกับทั้งปี
    url: String, // URL ข่าวที่สร้างจาก id
    url_image: String // URL รูปภาพที่สร้างจาก thumbnail
)
