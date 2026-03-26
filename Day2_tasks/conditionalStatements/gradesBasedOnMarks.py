# Write a program to assign grades based on marks (for example: A, B, C, Fail)

Marks=int(input("Enter marks out of 100:"))
if Marks>=90:
    print("Grade A")
elif Marks>=75 and Marks<90:
    print("Grade B")
elif Marks>=45 and Marks<75:
    print("Grade C")
else:
    print("FAIL")