"""Lab 06.03 - Binary Search"""
import json
class Student:
    def __init__(self,std_id : int = None,name : str= None,gpa : float = None):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    
    def get_std_id(self):
        return self.__std_id
    
    def get_name(self):
        return self.__name
    
    def get_gpa(self):
        return self.__gpa
    
    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

def main():
    """main"""
    lis = json.loads(input())
    namedata = input()
    begin = 0
    end = len(lis)-1
    min = (begin+end)//2
    comparisons = 0
    
    def find(min):
        l = [lis[min]["name"],namedata]
        l.sort()
        if l.index(lis[min]["name"]) > l.index(namedata):
            return True
        return False
    n=0
    while begin<=end:
        comparisons +=1
        if namedata == lis[min]["name"]:
            n = 1
            print(f"Found {lis[min]["name"]} at index {min}")
            s = Student(lis[min]["id"],lis[min]["name"],lis[min]["gpa"])
            s.print_details()
            break
        else:
            if find(min):
                end=min-1
                min=(begin+end)//2
            else:
                begin=min+1
                min = (begin+end)//2
    if not n:
        print(f"{namedata} does not exists.")
    print(f"Comparisons times: {comparisons}")
main()
