"""Lab 04.01 - Create BSTNode"""
class BSTNode:
    def __init__(self):
        self.data : int = None
        self.left = None
        self.right = None
def main():
    """mian"""
    bSTNode= BSTNode()
    bSTNode.data = int(input())
    print(bSTNode.data)
    print(bSTNode.left)
    print(bSTNode.right)
main()
