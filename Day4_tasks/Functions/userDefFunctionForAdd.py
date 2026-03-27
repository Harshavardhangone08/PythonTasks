# Write a program using a user-defined function to add two numbers.

def add(a,b):
    return a+b

n1,n2=map(int,input("Enter value of n1 and n2 seperated by space:").split())
s=add(n1,n2)
print("Sum of two numbers:",s)