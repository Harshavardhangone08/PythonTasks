'''
. Employee Salary System (Simple Inheritance)
A company has two types of employees: Employee and Manager. Create a base class
Employee containing name and salary. Create a derived class Manager that inherits
from Employee and displays the employee details.
'''
class Employee:
    def details(self,name,salary):
        print(f"{name} : {salary}")
    
class Manager(Employee):
    pass

name=input("Enter employee name:")
salary=float(input("Enter salary:"))

E=Manager()
E.details(name,salary)