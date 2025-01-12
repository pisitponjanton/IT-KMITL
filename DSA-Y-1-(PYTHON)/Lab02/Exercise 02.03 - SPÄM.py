"""Exercise 02.03 - SPÄM"""
class Matching:
    def __init__(self,data,type):
        self.data = data
        self.type = type
        self.listB = list()
    def is_parentheses_matching(self):
        newdata = [i for i in self.data if i in self.type]
        newdata2 = newdata.copy()
        for i in newdata2:
            if i == self.type[0]:
                self.listB.append(i)
                newdata.pop()
            elif i == self.type[1]:
                try:
                    self.listB.pop()
                    newdata.pop()
                except:
                    print("Underflow: Cannot pop data from an empty list")
        if self.listB or newdata:
            return False
        return True
inp = input()
l1,l2,l3 = [i for i in inp if i in "()"],[i for i in inp if i in "{}"],[i for i in inp if i in "[]"]
matching1,matching2,matching3 = Matching(list(l1),"()"),Matching(list(l2),"{}"),Matching(list(l3),"[]")
def main():
    """main"""
    boolean1,boolean2,boolean3 = matching1.is_parentheses_matching(),matching2.is_parentheses_matching(),matching3.is_parentheses_matching()
    print(boolean1 and boolean2 and boolean3)
main()
