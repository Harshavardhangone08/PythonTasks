'''
Student Information System (Class & Object)
A school wants a program to store student details. Create a Student class with
attributes such as name, roll number, and marks. Create objects for at least three
students and display their details.
'''
class Student:
    def details(self,name,rollNo,marks):
       print(f"{rollNo}.{name}: {marks}")
 
s=Student()
s.details("Harsha",4,986)
s.details("Vardhan",16,950)
s.details("Arjun",20,975)
