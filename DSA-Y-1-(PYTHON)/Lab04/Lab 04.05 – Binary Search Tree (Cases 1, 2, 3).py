"""Lab 04.05 – Binary Search Tree (Cases 1, 2, 3)"""
class BSTNODE:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = BSTNODE(data)
        else:
            self._insert(self.root,data)
            
    def _insert(self,node,data):
        if node.data > data:
            if node.left is None:
                node.left = BSTNODE(data)
            else:
                self._insert(node.left,data)
        else:
            if node.right is None:
                node.right = BSTNODE(data)
            else:
                self._insert(node.right,data)
                
    def delete(self,data):
        if self.root is None:
            print("Delete Error,",data,"is not found in Binary Search Tree.")
        else:
            self.root = self._delete(self.root,data)

    def _delete(self,node,data):
        if node is None:
            print("Delete Error,",data,"is not found in Binary Search Tree.")
            return None
        if node.data > data:
            node.left = self._delete(node.left,data)
        elif node.data < data:
            node.right = self._delete(node.right,data)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                maxleft = node.left
                while not maxleft.right is None:
                    maxleft = maxleft.right
                self.delete(maxleft.data)
                node.data = maxleft.data
        return node
    def preorder(self):
        return self._preorder(self.root)
    def _preorder(self,node):
        if node is None:
            return "".split()
        left = self._preorder(node.left)
        right = self._preorder(node.right)
        return str(node.data).split() + left + right
    
    def inorder(self):
        return self._inorder(self.root)
    def _inorder(self,node):
        if node is None:
            return "".split()
        left = self._inorder(node.left)
        right = self._inorder(node.right)
        return left + str(node.data).split() + right
    
    def postorder(self):
        return self._postorder(self.root)
    def _postorder(self,node):
        if node is None:
            return "".split()
        left = self._postorder(node.left)
        right = self._postorder(node.right)
        return left + right + str(node.data).split()
    
    def is_empty(self):
        return self.preorder() and self.inorder() and self.postorder()
    
    def traverse(self):
        if self.is_empty():
            print("Preorder: -> "+" -> ".join(self.preorder()))
            print("Inorder: -> "+" -> ".join(self.inorder()))
            print("Postorder: -> "+" -> ".join(self.postorder()))
        else:
            print("This is an empty binary search tree.")
def main():
    my_bst = BST()
    while True:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        data = int(data)
        if condition == "I":
            my_bst.insert(data)
        elif condition == "D":
            my_bst.delete(data)
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()