"""Labs 06.02 - ProbHash Hashing"""
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
        
class ProbHash:
    def __init__(self,size):
        self.__hash_table :list= list()
        self.__size :int = size
            
    def hash(self,key):
        return key%self.__size

    def rehash(self,hkey):
        return hkey+1
    
    def find_data(self,index):
        ind = self.hash(index)
        while self.__hash_table[ind] is not None:
            ind = self.rehash(ind)
            if None not in self.__hash_table:
                break
            if ind >= self.__size:
                ind=0
        return ind

    def insert_data(self,std:Student):
        if not self.__hash_table:
            for _ in range(self.__size):
                self.__hash_table.append(None)
            
        index = self.find_data(std.get_std_id())
        
        if None not in self.__hash_table:
            print(f"The list is full. {std.get_std_id()} could not be inserted.")
            return
        self.__hash_table[index] = std
        print(f"Insert {std.get_std_id()} at index {index}")
    
    def search_data(self,std_id):
        for index,i in enumerate(self.__hash_table):
            if i is None:
                continue
            if i.get_std_id() == std_id:
                print(f"Found {i.get_std_id()} at index {index}")
                return i
        print(f"{std_id} does not exist.")
        return None
    
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()