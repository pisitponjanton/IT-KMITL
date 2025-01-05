"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        elif data < self.data:
            if self.left is None:
                self.left = BST(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
            else:
                self.right.insert(data)

    def preorder(self):
        result = self._preorder(self)
        print(" -> ".join(result))

    def _preorder(self,node):
        if node is None:
            return "".split()
        left = self._preorder(node.left)
        right = self._preorder(node.right)
        return str(node.data).split() + left + right

def main():
    """main()"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ->", end=" ")
    my_bst.preorder()

main()
