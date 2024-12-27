"""Lab 03.04 – Singly Linked List (Insert Before)"""
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
        if node not in self.head:
            print("Cannot insert,",node,"does not exist.")
        else:
            newhead = self.head.split(" -> ")
            index = newhead.index(node)
            newhead.insert(index,data)
            self.head = ""
            for i in newhead:
                self.head += i+" "
            self.head = self.head.strip().replace(" "," -> ")
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