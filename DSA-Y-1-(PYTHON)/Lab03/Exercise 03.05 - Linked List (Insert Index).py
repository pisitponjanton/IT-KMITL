"""Exercise 03.05 - Linked List (Insert Index)"""
class Linked:
    def __init__(self):
        self.data = ""
    def insertL(self,n,data):
        lis = self.data.strip().split()
        lis.insert(n,data)
        self.data = lis
def main():
    """main"""
    linked = Linked()
    for _ in range(int(input())):
        linked.data += input()+" "
    linked.insertL(int(input()),input())
    print(*linked.data)
main()
