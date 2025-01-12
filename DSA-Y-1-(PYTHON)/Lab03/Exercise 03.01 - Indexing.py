"""Exercise 03.01 - Indexing"""
class Indexing:
    def __init__(self):
        self.data = ""
    def indexC(self,ind):
        if self.data:
            newlis = self.data.strip().split("    ")
            for i,j in enumerate(newlis):
                if i == ind or ind == i-len(newlis):
                    return j
        return "Error"
def main():
    """main"""
    indexing = Indexing()
    while True:
        inp = input()
        if inp == "Last":
            break
        indexing.data += inp+"    "
    print(indexing.indexC(int(input())))
main()