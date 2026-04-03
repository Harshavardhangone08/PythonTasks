'''
. Student Attendance Record
A teacher wants to store student attendance in a file named attendance.txt. Write a
Python program that takes a student name as input and appends it to the file. Then
display the contents of the file.
'''

Stu_name=input("Enter the name of the Student:")
Stu=open("attendance.txt","a")
Stu.write(f"{Stu_name} \n")
Stu.close()

print("Attendance list of Students")
Stu=open("attendance.txt",'r')
print(Stu.read())
Stu.close()