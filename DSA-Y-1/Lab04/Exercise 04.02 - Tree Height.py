"""Exercise 04.02 - Tree Height"""
class BST:
    def __init__(self,data = None):
        self.data = data
        self.left = None
        self.right = None
        self.count = 0
    def insert(self,data):
        if self.data is None:
            self.data = data
        elif self.data > data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)
    def high(self):
        if self is None:
            return 0
        left_height = self.left.high() if self.left else 0
        right_height = self.right.high() if self.right else 0
        return 1 + max(left_height, right_height)

def main():
    """main()"""
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        _, data = text.split(": ")
        my_bst.insert(int(data))
    print(my_bst.high())
main()
