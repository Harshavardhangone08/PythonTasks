''' Write a program to check whether a given number is an Armstrong number or not.
Definition:
A number is called an Armstrong number if the sum of the cubes of its digits is equal to the
number itself.
'''
def checkArmstrongNum(Num):
    original=Num
    sum_digits=0
    while(Num>0):
        a=Num%10
        sum_digits+=a**3
        Num=Num//10
    if original==sum_digits:
       print(f"{original} is Armstrong Number!")
    else:
        print(f"{original} is not an Armstrong Number!")        

try:
   Num=int(input("Enter a positive integer:"))
   checkArmstrongNum(Num)
except ValueError:
    print("Enter a valid Integer!")