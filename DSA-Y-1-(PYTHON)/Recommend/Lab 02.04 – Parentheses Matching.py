"""[Recommend] Lab 02.04 – Parentheses Matching"""
class Matching:
    def __init__(self):
        self.data = list()
    def stacker(self):
        copy_data = self.data.copy()
        lis = list()
        for i in self.data:
            try:
                if i == "(":
                    lis.append(i)
                else:
                    lis.pop()
                copy_data.pop()
            except:
                print("Underflow: Cannot pop data from an empty list")
        if copy_data or lis:
            return False
        return True
            
def main():
    """main"""
    matching = Matching()
    inp = input()
    for i in inp:
        if i in "()":
            matching.data.append(i)
    b = matching.stacker()
    print(f"Parentheses in {inp} are {"" if b else "un"}matched\n{b}")
main()
