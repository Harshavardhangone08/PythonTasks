'''
Advanced Simulation System 
Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics
'''
import numpy as np
import pandas as pd

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.grade=self.assign_grade()
        
    def assign_grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=75:
            return 'B'
        elif self.marks>=60:
            return 'C'
        elif self.marks>=40:
            return 'D'
        else:
            return 'F'
        
#Main program
try:
   n=int(input("Enter number of studens:"))
   stu=[]
   marks_arr=np.random.randint(20,100,n)
   for i in range(n):
       name=input(f"Enter name of student {i+1}:")
       marks=marks_arr[i]
       
       s=Student(name,marks)
       stu.append(s) #stores name marks grade
       
   #converting to Data Frame
   data={"Name":[x.name for x in stu],"Marks":[x.marks for x in stu],"grade":[x.grade for x in stu]}
   
   df=pd.DataFrame(data)
   print("Student report:")
   print(df)
   
   #statistics
   avg=sum(marks_arr)/len(marks_arr)
   maximum=max(marks_arr)
   minimum=min(marks_arr)
   
   print("Statistics:")
   print(f"Average:{avg:.2f}")
   print("Maximum:",maximum)
   print("Minimum:",minimum)
   
   with open("Student_Records","w") as file:
       file.write(df.to_string(index=False))
       file.write(f"\nAverage:{avg:.2f}")
       file.write(f"\nMaximum:{maximum}")
       file.write(f"\nMinimum:{minimum}")
   
except ValueError:
    print("Invalid input! Enter valid integer")