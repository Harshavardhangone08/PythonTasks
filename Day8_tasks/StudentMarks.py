'''
Student Marks File Analyzer
A teacher stores student marks in a file marks.txt in the format:
Name Marks
Example:
Rahul 80
Anita 90
Ravi 75
Write a Python program to:
● Read the file
● Display all student records
● Calculate and display the average marks of the class
'''
file=open("marks.txt","w")
N=int(input("Number of Students:"))
for i in range(N):
    name=input("Enter Student name:")
    marks=int(input("Marks:"))
    file.write(f"{name} {marks} \n")

file=open("marks.txt","r")
print("Student Records")
print(file.read())
file.close()

file = open("marks.txt", "r")

print("Average marks of the class")
total=0
count=0

for line in file:
    data = line.split()
    if len(data)==2:
        data=line.split()
        print(data[0], data[1])
    
        total= total+int(data[1])
        count+=1

file.close()

avg= total/count
print(f"Average Marks: {avg:.2f}")
