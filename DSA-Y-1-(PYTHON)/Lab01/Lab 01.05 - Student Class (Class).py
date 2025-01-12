"""Lab 01.05 - Student Class (Class)"""
class Student:
    def __init__(self,name,fm,age,id,gpa):
        self.name = name
        self.fm = fm
        self.age = age
        self.id = id
        self.gpa = gpa
def main():
    """Lab 01.04 - Student Class (No Class)"""
    l=[]
    for _ in range(3):
        l.append(Student(input(),input(),input(),input(),input()))
    x = input()
    o=[]
    for i in l:
        if x == i.id:
            text = "Miss" if i.fm == "Female" else "Mr"
            o=i
            break
    if o:
        print(text,o.name,"("+o.age+")","ID:",x,"GPA",f"{float(o.gpa):.2f}")
    else:
        print("Student not found")
main()
            