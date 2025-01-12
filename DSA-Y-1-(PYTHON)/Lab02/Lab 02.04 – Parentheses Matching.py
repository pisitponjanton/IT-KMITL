"""Lab 02.04 – Parentheses Matching"""
class Matching:
    def __init__(self,data,listB=list()):
        self.data = data
        self.listB = listB
    def is_parentheses_matching(self):
        newdata = list()
        for i in self.data:
            if i in "()":
                newdata.append(i)
        newdata2 = newdata.copy()
        for i in newdata2:
            if i == "(":
                self.listB.append(i)
                newdata.pop()
            elif i == ")":
                try:
                    self.listB.pop()
                    newdata.pop()
                except:
                    print("Underflow: Cannot pop data from an empty list")
        if self.listB or newdata:
            return False
        else:
            return True
inp = input()
matching = Matching(list(inp))
def main():
    """main"""
    boolean = matching.is_parentheses_matching()
    print(f"Parentheses in {inp} are matched\n{boolean}" if boolean else 
          f"Parentheses in {inp} are unmatched\n{boolean}")
main()
