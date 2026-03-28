# Write a recursive function to calculate the factorial of a number.

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

Num=int(input("Enter a positive number:"))
f=fact(Num)
print(f"Factorial of {Num}: {f}")

