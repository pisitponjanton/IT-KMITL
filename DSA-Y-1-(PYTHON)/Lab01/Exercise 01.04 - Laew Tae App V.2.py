"""Exercise 01.04 - Laew Tae App V.2"""
class Foods:
    def __init__(self,num):
        self.num = num
    def add_food_item(self):
        l = ['Fried Chicken', 'Hamburger', 'Pizza', 'Steak']
        for _ in range(self.num):
            l.append(input())
        l.sort()
        return l
print(Foods(int(input())).add_food_item())
            