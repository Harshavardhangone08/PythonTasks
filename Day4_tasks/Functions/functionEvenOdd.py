# Write a function to check whether a number is even or odd.

def evenOdd(n):
    if n%2==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

num=int(input("Enter a number:"))
evenOdd(num)