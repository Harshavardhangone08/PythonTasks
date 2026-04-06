'''
Vehicle Management System (Inheritance)
A transport company manages different vehicles. Create a base class Vehicle with
attributes like brand and speed. Create derived classes Car and Bike that inherit from
Vehicle and display their details.
'''
class Vehicles:
    car_brand="BMW"
    car_speed='150 KMPH'
    bike_brand="Royal Enfield"
    bike_speed='120 KMPH'
class car(Vehicles):
    def car_details(self):
        print(f"car brand {self.car_brand} and speed {self.car_speed}")
class bike(Vehicles):
    def bike_details(self):
        print(f"Bike brand {self.bike_brand} and speed {self.bike_speed}")
c=car()
b=bike()
c.car_details()
b.bike_details()    
        
