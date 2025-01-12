"""Exercise 03.04 - Bus Stop"""
class BusStop:
    def __init__(self):
        self.datalis = "".split()
        self.nbus = 0
        self.countdata = 0
    def sortt(self,x):
        for i in x.split():
            return int(i)
    def dowmBus(self,num,newdata):
        nn = newdata.copy()
        for i in nn:
            if num == int(i):
                newdata.remove(i)
                self.countdata+=1
        return newdata
    def Bus(self):
        newdata = "".split()
        self.datalis.sort(key=lambda x: self.sortt(x))
        for i1,i in enumerate(self.datalis):
            newdata = self.dowmBus(i1+1,newdata)
            for j in i.split():
                if i1+1 < int(j) and len(newdata)<self.nbus:
                    newdata += j.split()
                elif len(newdata)>=self.nbus:
                    break
def main():
    """main"""
    busStop = BusStop()
    busStop.nbus = int(input())
    for _ in range(int(input())):
        inp = input()+"BusStop"
        busStop.datalis += inp.strip("BusStop").split("BusStop")
    busStop.Bus()
    print(busStop.countdata)
main()
