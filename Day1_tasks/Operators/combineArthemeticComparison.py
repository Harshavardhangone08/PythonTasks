# Combine arithmetic and comparison operators in one expression.
a1=int(input("Enter Angle 1:"))
a2=int(input("Enter Angle 2:"))
if a1 and a2 != 0:
    if a1+a2==90:
        print("Both are complementary angles")
    elif a1+a2==180:
        print("Both are supplementary angles")
    else:
        print("The given angles are neither complementary nor supplementary")
else:
    print("Enter valid values")
    

