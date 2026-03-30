'''
Write a program to check whether a given number is a Strong number.
Definition:
A Strong number is a number whose sum of factorial of digits is equal to the number itself.
'''

import math
def checkStrongNum(Num):
    if Num==0:
        print("0 is Not a Strong Number")
        return
    
    original=Num
    facto_sum=0
    while(Num>0):
        a=Num%10
        facto_sum+=math.factorial(a)
        Num=Num//10
    if original==facto_sum:
        print(f"{original} is a Strong Number")
    else:
        print(f"{original} is not a Strong Number")

try:
    Num=int(input("Enter a number:"))
    if Num<0:
        print("Enter a positive integer")
    else:
        checkStrongNum(Num)
except ValueError:
    print("Enter a valid integer!")