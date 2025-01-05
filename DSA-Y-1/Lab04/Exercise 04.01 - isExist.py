"""Exercise 04.01 - isExist"""
class BST:
    def __init__(self):
        self.data = "".split()
    def isExist(self,data):
        return data in self.data
def main():
    bst = BST()
    while 1:
        num = input()
        if "Done" == num:
            break
        bst.data += num.split("I: ")
    print(bst.isExist(input()))
main()
        