class Item:
    def __init__(self,name:str,price:int,weight:float):
        self.__name = name
        self.__price = price
        self.__weight = weight
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_weight(self):
        return self.__weight

def main():
  import json
  item_in = json.loads(input())
  item = Item(item_in["name"], item_in["price"], item_in["weight"])
  print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()