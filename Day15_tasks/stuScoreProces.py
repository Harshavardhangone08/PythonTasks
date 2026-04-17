'''
Student Score Processor 
Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file
'''
#import math

Stu=[("Harsha",92),("Jhon",40),("Vardhan",85),("Raju",48),("Kriti",74)]

Stu_di=dict(Stu)
print("Dictionary:",Stu_di)

Passed_stu={}
for k,val in Stu_di.items():
    if val>50:
      Passed_stu[k]=val

print("Passed Students:",Passed_stu)

total=sum(Passed_stu.values())
count=len(Passed_stu)
avg=total/count

print(f"Average:{avg:.2f}")

#Storing in a file

with open("Student_score",'w') as file:
    file.write("Records of passed Students\n")
    for name,marks in Passed_stu.items():
        file.write(f"{name} {marks}\n")
    file.write(f"\nAverage of Marks:{avg:.2f}")