# Write a program to check whether a number is even or odd.
num=int(input("Enter a number"))
'''
# normal method
if num%2==0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")
    '''
# using Logical AND (&) operator

if num & 1==0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")