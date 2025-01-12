"""Exercise 03.03 - AlmostMean"""
class AlmostMean:
    def __init__(self):
        self.data = ""
        self.numdata = ""
        self.alldata = ""
        self.xbardata = 0
        self.find_strdata = ""
    def xbar(self):
        n = self.numdata.strip().split()
        self.xbardata = sum(float(i) for i in n)/len(n)
    def findxbar(self):
        n = self.numdata.strip().split()
        n.sort(key=lambda x: -float(x))
        for i in n:
            if float(i) < self.xbardata:
                self.find_strdata = i
                break
    def finddata(self):
        for i in self.alldata.strip("+").split("+"):
            if self.find_strdata in i:
                return i
def main():
    """main"""
    almostmean = AlmostMean()
    for _ in range(int(input())):
        inp = input()
        almostmean.alldata += inp+"+"
        for j,i in enumerate(inp.split()):
            if not j:
                almostmean.data += i+" "
            else:
                almostmean.numdata += i+" "
    almostmean.xbar()
    almostmean.findxbar()
    print(almostmean.finddata())
main()
