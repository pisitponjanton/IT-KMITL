"""[Recommend] Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
class DataNode:
    def __init__(self,data :str = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def traverse(self):
        if self.head is None:
            print("This is an empty list.")
            return
        newObject = self.head
        count=0
        while newObject is not None:
            if not count:
                print(newObject.data,end="")
                count=1
            else:
                print(" -> "+newObject.data,end="")
            newObject = newObject.next
    
    def insert_last(self,data):
        if self.head is None:
            self.head = DataNode(data)
        else:
            newObject = self.head
            if newObject.next is None:
                newObject.next = DataNode(data)
            else:
                while newObject.next is not None:
                    newObject = newObject.next
                newObject.next = DataNode(data)
    
    def insert_front(self,data):
        if self.head is None:
            self.head = DataNode(data)
        else:
            newNode = DataNode(data)
            newNode.next = self.head
            self.head = newNode
    
    def insert_before(self,node, data):
        backNode = None
        newObject = self.head
        while newObject is not None:
            if newObject.data == node:
                if backNode is None:
                    newNode = DataNode(data)
                    newNode.next = self.head
                    self.head = newNode
                    return
                else:
                    backNode.next = DataNode(data)
                    backNode.next.next = newObject
                    return
            backNode = newObject
            newObject = newObject.next
        print("Cannot insert, "+node+" does not exist.")
    
    def delete(self,data):
        backNode = None
        newObject = self.head
        while newObject is not None:
            if newObject.data == data:
                if backNode is None:
                    self.head = self.head.next
                else:
                    if backNode.next.next is not None:
                        backNode.next = backNode.next.next
                    else:
                        backNode.next = backNode.next
                return
            backNode = newObject
            newObject = newObject.next
        print("Cannot delete, "+data+" does not exist.")
def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
        mylist.insert_before(*data.split(", "))
    elif condition == "D":
        mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()
main()