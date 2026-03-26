# Write a program to find the largest of three numbers using if-elif-else

a,b,c=10,18,25

if a>b:
    if a>c:
        print("a is greater than b and c")
    else:
        print("c is greater than a and b")
elif b>c:
    print("b is greater than a and c")
else :
    print("c is greater than a and b")