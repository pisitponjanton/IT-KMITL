"""Lab 01.06 - Rectangle"""
class Rectangle:
    def __init__(self, height, width):
        """Lab 01.06 - Rectangle"""
        self.height = height
        self.width = width

    def calculate_area(self):
        """Lab 01.06 - Rectangle"""
        return self.height * self.width

    def calculate_perimeter(self):
        """Lab 01.06 - Rectangle"""
        return self.height*2 + self.width*2
    
rectangle = Rectangle(float(input()), float(input()))

condition = input()
if condition == "area":
  result = rectangle.calculate_area()
else:
  result = rectangle.calculate_perimeter()
print(f"{result:.2f}")
