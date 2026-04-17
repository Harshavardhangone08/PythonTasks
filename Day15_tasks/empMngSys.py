'''
Employee Management System (OOP + File + Dict) 
Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees 
'''
class Employee:
    def __init__(self,name,salary):
       self.name=name
       self.salary=salary
data={}
try:
    n=int(input("Enter number of Employees:"))
    
    for i in range(n):
      while True:
        name=input("Enter Employee name:")
        try:
            salary=float(input("Enter salary:"))
            break
        except ValueError:
            print("Invalid salary!Please enter again")
            
        
      emp=Employee(name,salary)
      data[name]=emp
        
except ValueError:
    print("Invalid input")
 
with open("Employee.txt","w") as emp_file:
    for emp in data.values():
        emp_file.write(f"{emp.name} {emp.salary}\n")
        
print("Employee details")
for emp in data.values():
    print(f"{emp.name} {emp.salary}")  