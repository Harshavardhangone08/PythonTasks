'''
Question:
Write a program to check whether a number is a Perfect number.
Definition:
A Perfect number is a number whose sum of proper divisors equals the number.
'''
def checkPerfectNum(Num):
    if Num<=1:
        print(f"{Num} is not a Perfect Number")
        return
    total=1 # 1 divides every Number
    for i in range(2,Num//2+1):
        if Num%i==0:
            total+=i
    if total==Num:
        print(f"{Num} is a Perfect Number")
    else:
        print(f"{Num} is not a Perfect Number")

try:
    Num=int(input("Enter a number:"))
    checkPerfectNum(Num)
except ValueError:
    print("Enter an Integer value!")