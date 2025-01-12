"""Exercise 01.02 - Elevator"""
class Elevator:
    def __init__(self,maxfloor):
        """class Elevator"""
        self.maxfloor = maxfloor
    def invalid_Floor(self,x):
        """invalid Floor"""
        num=0
        for i in x:
            if i>self.maxfloor:
                num+=1
        return num
def inputm():
    """input"""
    x=[]
    num=int(input())
    while True:
       y = input()
       if y == "Done":
           break
       x.append(int(y))
    e1 = Elevator(num).invalid_Floor(x)
    for _ in range(e1):
        print("Invalid Floor!")
    x = [i for i in x if i <=num ]
    print(x[-1] if x else 1)
inputm()