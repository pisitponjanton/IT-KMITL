"""Lab 02.02 - Student Groups"""
class Student:
    def __init__(self,groups,data=list(),newlist = list()):
        self.groups = groups
        self.data = data
        self.newlist = newlist
        
    def loop(self):
        for _ in range(self.groups):
            list1=list()
            x = self.data.pop()
            list1.append(x)
            self.newlist.append(list1)
        while self.data:
            for i in self.newlist:
                if not self.data:
                    break
                x = self.data.pop()
                i.append(x)
student = Student(int(input()))
def main():
    """main"""
    for _ in range(int(input())):
        student.data.append(input())
    student.loop()
    for i,i1 in enumerate(student.newlist):
        print(f"Group {i+1}: ",end="")
        for j,j1 in enumerate(i1):
            if j != len(i1)-1:
                print(j1,end=", ")
            else:
                print(j1)
main()
