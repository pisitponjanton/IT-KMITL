"""[Recommend] Lab 03.01 - Create DataNode"""
class DataNode:
    def __init__(self,data :str = None):
        self.data = data
        self.next = None

def main():
    data = input()
    node = DataNode(data)
    print(node.data)
    print(node.next)
main()