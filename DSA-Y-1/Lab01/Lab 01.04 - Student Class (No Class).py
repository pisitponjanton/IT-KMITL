"""Lab 01.04 - Student Class (No Class)"""
def main():
    """Lab 01.04 - Student Class (No Class)"""
    l=[]
    for _ in range(3):
        l1=[]
        for _ in range(5):
            l1.append(input())
        l.append(l1)
    x = input()
    o=[]
    for i in l:
        if x == i[3]:
            text = "Miss" if i[1] == "Female" else "Mr"
            o=i
            break
    if o:
        print(text,o[0],"("+o[2]+")","ID:",x,"GPA",f"{float(o[-1]):.2f}")
    else:
        print("Student not found")
main()
