"""Labs 06.01 - Student Class"""
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
        
def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())