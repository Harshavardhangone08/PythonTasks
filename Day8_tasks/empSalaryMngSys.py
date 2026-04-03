'''
Employee Salary Management System
A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file
'''
file=open("employee.txt","r")
print(file.read())
file.close()
employees=[]
file=open("employee.txt", "r")
for line in file:
    data=line.split()
    if len(data)==2:
        name=data[0]
        salary=float(data[1])
        employees.append((name, salary))
file.close()
if len(employees) > 0:
    highest=employees[0]

    for emp in employees:
        if emp[1] > highest[1]:
            highest=emp

    print("\nHighest Salary:")
    print(highest[0], highest[1])
else:
    print("No data found")
file.close()

file = open("employee.txt", "a")

name = input("\nEnter new employee name: ")
salary = int(input("Enter salary: "))

file.write("\n"+name + " " + str(salary) + "\n")

file.close()

print("New employee added")    