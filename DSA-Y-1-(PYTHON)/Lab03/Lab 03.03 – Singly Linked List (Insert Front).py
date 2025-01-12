"""Lab 03.03 – Singly Linked List (Insert Front)"""
class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = ""
    def insert_front(self,data):
        self.count+=1
        if not self.head:
            self.head = data
        else:
            self.head = data + " -> " + self.head
    def insert_last(self,data):
        self.count+=1
        if not self.head:
            self.head = data
        else:
            self.head += " -> "+data
    def insert_before(self,node,data):
        self.count+=1
        newhead = ""
        if not node in self.head:
            print("Cannot insert,",node,"does not exist.")
        else:
            for i in self.head.split():
                if i == node:
                    lis = data + " -> " + i
                else:
                    lis = i
                newhead += lis+" "
            self.head = newhead.strip()
    def traverse(self):
        print(self.head if self.head else "This is an empty list.")
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
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()