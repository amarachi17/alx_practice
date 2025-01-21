class Shape:
    def calculate_area(self):
        print("Cannot calculate area")
        
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calculate_area(self):
        return self.width * self.height
    
    
rectangle = Rectangle(5, 10)
print("Area of Rectangle: ", rectangle.calculate_area())
