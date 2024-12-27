"""Exercise 03.02 - Taking Turns"""
class TakingTurns:
    def __init__(self):
        self.data = ""    
    def front(self,newlis,newdata):
        prelis = ''
        for i,j in enumerate(newlis):
            if not i:
                newdata += " -> "+j
            else:
                prelis += j+" "
            newlis =  prelis.strip().split()
        return newlis,newdata
    def back(self,newlis,newdata):
        if not newdata:
            newdata = newlis.pop()
        else:
            newdata += " -> " + newlis.pop()
        return newlis,newdata
    def traverse(self):
        newdata = ""
        count = 0
        newlis = self.data.strip().split()
        newlis,newdata = self.back(newlis,newdata)
        for _ in range(len(newlis)):
            if count in (0,1):
                newlis,newdata = self.front(newlis,newdata)
            else:
                newlis,newdata = self.back(newlis,newdata)
            count+=1
            if count == 4:
                count = 0
        return newdata
def main():
    """main"""
    takingTurns = TakingTurns()
    for _ in range(int(input())):
        takingTurns.data += input()+" "
    print(takingTurns.traverse())
main()
