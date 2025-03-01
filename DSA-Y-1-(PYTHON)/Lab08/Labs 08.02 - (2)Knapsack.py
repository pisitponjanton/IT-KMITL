"""Labs 08.02 - (2)Knapsack"""
import json
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
def knapsack(item: Item):
    """Knapsack"""
    return item.get_price()/item.get_weight()
def main():
    item_list = []
    sum = 0
    for _ in range(int(input())):
        iput = json.loads(input())
        item_list.append(Item(iput["name"],iput["price"],iput["weight"]))
    kg = float(input())
    item_list.sort(key=knapsack,reverse=True)
    print(f"Knapsack Size: {kg} kg")
    print("===============================")
    for i in item_list:
        if kg >= i.get_weight():
            print(f"{i.get_name()} -> {i.get_weight()} kg -> {i.get_price()} THB")
            sum +=i.get_price()
            kg-= i.get_weight()
    print(f"Total: {sum} THB")
main()