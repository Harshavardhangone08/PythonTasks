'''
Rectangle Area Calculator (Constructor)
A geometry application needs to calculate the area of rectangles. Create a Rectangle
class that uses a constructor to initialize length and width. Add a method to calculate
and display the area.
'''
class Student:
    def __init__(self):
        self.length=20
        self.breadth=10
    def rectangleArea(self):
        area=self.length*self.breadth
        print("Area of Rectangle:",area)

R=Student()
R.rectangleArea()