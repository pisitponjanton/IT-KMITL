package model

// case class สำหรับเก็บข้อมูลข่าวที่ผ่านการคำนวณสถิติรายปีแล้ว
// โดยเพิ่มข้อมูลปี (year), ยอดรวมทั้งปี (totalByYear)
// และเปอร์เซ็นต์การเข้าชมเทียบกับทั้งปี (viewPercent)
case class RecordWithYearPercent(
    id: String, // รหัสข่าว
    title: String, // ชื่อข่าว
    thumbnail: String, // path รูปภาพ
    slug: String, // slug สำหรับ URL
    primaryTag: String, // tag หลัก
    isShowComment: String, // flag แสดง/ซ่อน comment
    createdAtdatetime: String, // วันที่และเวลาเผยแพร่
    description: String, // คำอธิบายข่าว
    shareCount: Long, // จำนวนการแชร์
    commentCount: Long,

    // --- Derived / Aggregated Columns ---
    viewCount: Long, // จำนวนการเข้าชมของข่าวนี้
    year: Int, // ปีที่ดึงจาก createdAtdatetime
    totalByYear: Long, // ยอดรวม viewCount ทั้งหมดของปีนั้น
    viewPercent: Double // เปอร์เซ็นต์ view ของข่าวนี้เทียบกับทั้งปี
)
