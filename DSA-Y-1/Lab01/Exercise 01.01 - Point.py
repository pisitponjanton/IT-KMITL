"""Exercise 01.01 - Point"""
class Point:
    def __init__(self,x1,y1,x2,y2):
        """Exercise 01.01 - Point"""
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def main(self):
        """Exercise 01.01 - Point"""
        return ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**0.5
point1 = Point(float(input()),float(input()),float(input()),float(input())).main()
print(f"{point1:.2f}")