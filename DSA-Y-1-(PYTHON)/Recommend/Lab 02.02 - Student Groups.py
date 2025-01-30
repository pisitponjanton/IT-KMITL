"""[Recommend] Lab 02.02 - Student Groups"""
class Student:
    def __init__(self,groups):
        self.data = list()
        self.groups = groups
        self.newdata = list()
    def stack(self):
        for _ in range(self.groups):
            x = list()
            x.append(self.data.pop())
            self.newdata.append(x)
        while self.data:
            for i in self.newdata:
                if not self.data:
                    break
                i.append(self.data.pop())
        for i,i1 in enumerate(self.newdata):
            print(f"Group {i+1}: ",end="")
            for j,j1 in enumerate(i1):
                if not j:
                    print(j1,end="")
                else:
                    print(", "+j1,end="")
            print()
            
def main():
    """main"""
    student = Student(int(input()))
    for _ in range(int(input())):
        student.data.append(input())
    student.stack()
main()