"""Music Box ( 14 คะแนน )"""
class Song:
    def __init__(self,name,genre,duration):
        self.name :str = name
        self.genre :str = genre
        self.duration :int = duration
        
    def show_info(self):
        return str(self.name+" <|> "+self.genre+" <|> "+f"{int(self.duration)//60}.{int(self.duration)%60:>02}")
    
class Undo:
    def __init__(self):
        self.data = None
        self.next = None
        
class Queue:
    def __init__(self):
        self.data = None
        self.next = None
        self.memo = Undo()
        
    def _zetMemo(self):
        newMemo = self
        memo = Queue()
        if newMemo.data is None:
            return
        while newMemo is not None:
            memo.enqueue_for_memo(newMemo.data)
            newMemo = newMemo.next
        if self.memo.data is None:
            self.memo.data = memo
        else:
            oMemo = self.memo
            while oMemo.next is not None:
                oMemo = oMemo.next
            oMemo.next = Undo()
            oMemo.next.data = memo
        
            
    def enqueue_for_memo(self, item: "Song"):
        if self.data is None:
            self.data = item
        else:
            newNext = self
            while newNext.next is not None:
                newNext = newNext.next
            newNext.next = Queue()
            newNext.next.data = item
            
    def enqueue(self, item: "Song"):
        self._zetMemo()
        if self.data is None:
            self.data = item
        else:
            newNext = self
            while newNext.next is not None:
                newNext = newNext.next
            newNext.next = Queue()
            newNext.next.data = item
            
    def dequeue(self):
        self._zetMemo()
        if self.data is None:
            print("Underflow! Dequeue from an empty queue")
            return
        data = self.data
        if self.next is None:
            self.data = None
        else:
            self.data = self.next.data
            self.next = self.next.next
        return data
    
    def peek(self):
        if self.data is None:
            print("Underflow! peek from an empty queue")
        return self.data
    
    def isEmpty(self):
        if self.data is None:
            return True
        return False
    
    def show_Queue(self):
        if self.data is None:
            print("Queue is empty!")
            return
        count = 1
        newobject = self
        while newobject is not None:
            print(f"Queue#{count} {newobject.data.show_info()}")
            count+=1
            newobject = newobject.next
    
    def lastSong(self,time):
        if self.data is None:
            print("There is no song in this queue!")
            return
        alltime,timeobject = 0,self
        while timeobject is not None:
            alltime+=int(timeobject.data.duration)    
            timeobject = timeobject.next
        time = time%alltime if time>alltime else time
        alltime, count, newobject = 0, 0, self
        while newobject is not None:
            alltime += int(newobject.data.duration)
            count+=1
            if alltime >= time:
                break
            newobject = newobject.next
        print(f"Queue#{count} {newobject.data.show_info()}")
    
    def removeSong(self,name):
        self._zetMemo()
        if self.data is None:
            print(f"Can not Delete! {name} is not exist")
            return
        newobject = self
        newQ,count = Queue(),0
        while newobject is not None:
            if newobject.data.name == name:
                count=1
            else:
                newQ.enqueue_for_memo(newobject.data)
            newobject = newobject.next
        if not count:
            print(f"Can not Delete! {name} is not exist")
            return
        self.data = None
        self.next = None
        newobject = newQ
        while newobject is not None:
            self.enqueue_for_memo(newobject.data)
            newobject = newobject.next
            
    def _groupSong(self,group):
        count = 0
        print(f"{group}:",end=" ")
        newobject = self
        while newobject is not None:
            if newobject.data.genre == group:
                if not count:
                    print(newobject.data.name,end="")
                else:
                    print(f" | {newobject.data.name}",end="")
                count=1
            newobject = newobject.next
        print()
        
    def groupSong(self):
        if self.data is None:
            print("Nothing here! Please add some song")
            return
        self._groupSong("JPOP")
        self._groupSong("KPOP")
        self._groupSong("R&B")
            
    def undo(self):
        newObject = self.memo
        if newObject.next is None:
            new = newObject.data
            newObject.data = None
        else:
            while newObject.next.next is not None:
                newObject = newObject.next
            new = newObject.next.data
            newObject.next = None
        self.data = None
        self.next = None
        while new is not None:
            self.enqueue_for_memo(new.data)
            new = new.next
    
    def _rev_queue(self):
        newObject = self
        if newObject.next is None:
            data = newObject.data
            newObject.data = None
            return data
        while newObject.next.next is not None:
            newObject = newObject.next
        data = newObject.next
        newObject.next = None
        return data.data
    
    def rev_queue(self):
        self._zetMemo()
        newObject, count = self, 0
        while newObject is not None:
            count+=1
            newObject = newObject.next
        newObject = Queue()
        for _ in range(count):
            newObject.enqueue_for_memo(self._rev_queue())
        self.data = None
        self.next = None
        while newObject is not None:
            self.enqueue_for_memo(newObject.data)
            newObject = newObject.next
            
def main(): #อธิบายโค้ดในส่วนของ main()
    """this is main function"""
    q = Queue() #สร้าง Queue ว่างขึ้นมา
    while (choice := input()) != "End": #ลูปรับค่าไปเรื่อย ๆ จนกว่าจะเจอคำว่า End
        command, data = choice.split(": ") #แยก input ออกเป็น 2 ค่า คือ command ในการเรียกใช้แต่ละ methods และ data สำหรับใส่เป็น Arguments ของ methods นั้น ๆ ( ถ้ามี )
        match command: # ใช้ match-case เพื่อจับคู่คำสั่งการทำงาน
            case "enqueue":
                q.enqueue(Song(*data.split("|")))  # เพิ่ม object ที่สร้างจากคลาส Song เข้าไปที่ส่วนท้ายของคิว
            case "dequeue":
                temp = q.dequeue() # ทำการลบและคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp: # ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Dequeue item:", temp.show_info())
            case "peek":
                temp= q.peek() # ทำการคืนค่าข้อมูลส่วนหัวของคิว มาไว้ในตัวแปร temp
                if temp:# ถ้า temp ไม่เท่ากับ None ให้แสดงข้อความออกมา
                    print("Peek item:", temp.show_info())
            case "isEmpty":  # เรียกใช้ isEmpty เพื่อดูว่าคิวว่างหรือไม่
                print(q.isEmpty())
            case "showQueue": # เรียกใช้ showQueue เพื่อแสดงผลข้อมูลเพลงในคิวตามลำดับ
                q.show_Queue()
            case "lastSong":  # เรียกใช้ lastSong เพื่อดูข้อมูลเพลงสุดท้ายที่จะได้ฟัง
                q.lastSong(int(data))
            case "removeSong": # เรียกใช้ removeSong เพื่อลบเพลงนั้นๆ ออกจากคิว
                q.removeSong(data)
            case "groupSong": # เรียกใช้ groupSong เพื่อแสดงชื่อเพลงตามประเภทของเพลง
                q.groupSong()
            case "undo": # เรียกใช้ undo เพื่อย้อนคืนการทำงาน
                q.undo()
            case "rev": # เรียกใช้ rev ย้อนกลับลำดับของเพลงในคิว
                q.rev_queue()
    q.show_Queue() # แสดงข้อมูลเพลงในคิว ก่อนจะจบการทำงานของฟังก์ชัน
main()