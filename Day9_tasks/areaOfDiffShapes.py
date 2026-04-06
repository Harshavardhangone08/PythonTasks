'''
Shape Area Calculator (Polymorphism)
A graphics application needs to calculate the area of different shapes. Create classes
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate
polymorphism by calling the same method for different objects.
'''
class Circle():
    def area(self):
        self.radius=float(input("Enter radius of circle:"))
        self.area_c=3.14*self.radius*self.radius
        print(f"Area of Circle:{self.area_c:.2f}")
        
class Rectangle:
    def area(self):
        self.l=float(input("Enter length of the rectangle:"))
        self.b=float(input("Enter breadth of the rectangle:"))
        self.area_r=self.l*self.b
        print(f"Area of Rectangle:{self.area_r:.2f}")
        
class Triangle():
    def area(self):
        self.b=float(input("Enter base of the traingle:"))
        self.h=float(input("Enter height of the traingle:"))
        self.area_t=0.5*self.b*self.h
        print(f"Area of Traingle:{self.area_t:.2f}")
        
c=Circle()
c.area()
r=Rectangle()
r.area()
t=Triangle()
t.area()