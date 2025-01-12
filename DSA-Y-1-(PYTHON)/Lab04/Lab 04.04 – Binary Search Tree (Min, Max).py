"""Lab 04.04 – Binary Search Tree (Min, Max)"""
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
        return result
        
    def inorder(self):
        result = self._inorder(self)
        return result

    def postorder(self):
        result = self._postorder(self)
        return result

    def _preorder(self,node):
        if node is None:
            return "".split()
        left = self._preorder(node.left)
        right = self._preorder(node.right)
        return str(node.data).split() + left + right
    
    def _inorder(self,node):
        if node is None:
            return "".split()
        left = self._inorder(node.left)
        right = self._inorder(node.right)
        return left + str(node.data).split() + right
    
    def _postorder(self,node):
        if node is None:
            return "".split()
        left = self._postorder(node.left)
        right = self._postorder(node.right)
        return left + right +str(node.data).split()
    
    def is_empty(self):
        return not self.data is None
    
    def traverse(self):
        if self.is_empty():
            print("Preorder: -> ",end="")
            print(" -> ".join(self.preorder()))
            print("Inorder: -> ",end="")
            print(" -> ".join(self.inorder()))
            print("Postorder: -> ",end="")
            print(" -> ".join(self.postorder()))
        else:
            print("This is an empty binary search tree.")
    def find_max(self):
        if self.data is None:
            return None
        return max(self.postorder(),key=lambda x:int(x))
    def find_min(self):
        if self.data is None:
            return None
        return min(self.postorder(),key=lambda x:int(x))
def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())
main()
