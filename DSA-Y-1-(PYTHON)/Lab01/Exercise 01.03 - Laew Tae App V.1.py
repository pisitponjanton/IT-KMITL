"""Exercise 01.03 - Laew Tae App V.1"""
class Foods:
    def __init__(self,lis_food):
        """Foods"""
        self.lis_food = lis_food
    def list_foods(self):
        """list_foods"""
        self.lis_food.sort()
        return self.lis_food
print(Foods(["Pizza","Fried Chicken","Hamburger","Steak"]).list_foods())