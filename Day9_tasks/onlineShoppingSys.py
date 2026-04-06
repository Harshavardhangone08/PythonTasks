'''
Online Shopping System (Multilevel Inheritance)
An e-commerce company organizes products using multiple levels. Create classes
Product → ElectronicProduct → MobilePhone using multilevel inheritance and
display product details.
'''

class Product():
    def details(self):
        print("Product Details:")
class ElectronicProduct(Product):
    def electronic(self):
        print("This is an Electronic Device")
        
class MobilePhone(ElectronicProduct):
    def mobile(self):
        print("Mobile brand: Iqoo \ncost:30000 \nRAM:12GB \nStorage:256GB")

p=MobilePhone()
p.details()
p.electronic()
p.mobile()

    