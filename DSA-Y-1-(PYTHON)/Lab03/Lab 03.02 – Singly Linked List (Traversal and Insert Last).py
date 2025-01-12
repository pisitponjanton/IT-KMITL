"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = ""
    def insert_last(self,data):
        self.count+=1
        if not self.head:
            self.head = data
        else:
            self.head += " -> "+data
    def traverse(self):
        print(self.head if self.head else "This is an empty list.")
def main():
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input().strip())
    mylist.traverse()
main()
    