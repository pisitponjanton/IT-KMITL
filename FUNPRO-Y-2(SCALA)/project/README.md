# 📊 Scala Data Processing & Parallel Benchmark Project

โปรเจกต์นี้เป็นระบบประมวลผลข้อมูลข่าวจากไฟล์ CSV  
ออกแบบในรูปแบบ Functional Data Pipeline  
พร้อมเปรียบเทียบประสิทธิภาพระหว่างการทำงานแบบ

- Sequential (ทำงานตามลำดับ)
- Parallel (ทำงานแบบขนานด้วย Future)

และมีระบบ Benchmark สำหรับวัดเวลาและคำนวณ Speedup

---

# 🎯 Objectives

- ออกแบบ Data Pipeline ด้วย Scala
- ใช้ Functional Programming ในการจัดการข้อมูล
- เปรียบเทียบ Sequential vs Parallel
- ศึกษาการใช้ Future และ ExecutionContext
- ทดลองวัด Speedup จากการทำงานแบบขนาน

---

# 🏗 Architecture Overview

Data Pipeline Flow

Load File
↓
Parse → Record (Raw Model)
↓
Clear Data → CleanRecord
↓
Add URL → RecordWithUrl
↓
Year Aggregation → RecordWithYearPercent
↓
All Tasks → AllTasksRecord
↓
Export CSV

---

# 📦 Data Models

1. Record (Raw Data)
   เก็บข้อมูลดิบจากไฟล์ CSV ครบทุก column

2. CleanRecord
   คัดกรองข้อมูลที่ไม่ valid (เช่น id ว่าง)

3. RecordWithUrl
   เพิ่ม field:
   - url
   - url_image

4. RecordWithYearPercent
   เพิ่ม field:
   - year
   - totalByYear
   - viewPercent

5. AllTasksRecord
   รวมทุกขั้นตอน:
   - Clean
   - URL
   - Aggregation
   - Percent Calculation

---

# ⚙ Functional Design Patterns

- ใช้ Either สำหรับ Error Handling
- ใช้ Option สำหรับ Parsing
- ใช้ Future สำหรับ Parallel Processing
- ใช้ Generic CSV Writer สำหรับ export

---

# 🚀 Sequential vs Parallel

แต่ละ Task มี 2 เวอร์ชัน

Clear Data → clearSeq / clearParallel  
Add URL Column → addSeq / addParallel  
Year Aggregation → aggregateSeq / aggregateParallel  
All Tasks → runSeq / runParallel

---

# 📈 Benchmark System

ใช้ runBenchmark เปรียบเทียบเวลา

Speedup = SeqTime / ParTime

ตัวอย่างผลลัพธ์:

Task: Year Aggregation
Total Records: 50000
Seq time: 120 ms
Parallel time: 45 ms
Speedup: 2.6667

---

# ⏱ Timer Utility

- measureSeq → วัด synchronous block
- measureFuture → วัด Future (blocking ด้วย Await)
- ใช้ System.nanoTime() เพื่อความแม่นยำสูง

---

# 📤 Output

ไฟล์ CSV จะถูกสร้างใน:

src/main/resources/{folder}/

เช่น:

clearData/output_seq.csv
clearData/output_parallel.csv

---

# 🧠 Parallel Strategy

1. ตรวจสอบจำนวน CPU cores
2. แบ่งข้อมูลเป็น chunk
3. ประมวลผลแต่ละ chunk ด้วย Future
4. รวมผลลัพธ์ด้วย Future.sequence

---

# ▶ How to Run

sbt run

หรือรันผ่าน IDE

---

# 🏁 Summary

โปรเจกต์นี้เป็นตัวอย่างของ:

- Functional Data Processing
- Parallel Computation
- Performance Benchmarking
- Clean Architecture Design

เหมาะสำหรับการเรียนรู้ Scala และการศึกษา Parallel Programming
