'''
Write a program to check whether a number is Prime.
Definition:
A Prime number is a number that has only two factors: 1 and itself
'''

def checkPrimeNum(Num):
    if Num<=1:
        print(f"{Num} is not a Prime Number")
        return
    
    for i in range(2,Num//2+1):  # range(2,int(Num**0.5)+1)
        if Num%i==0:
            print(f"{Num} is not a Prime Number, It is a Composite Number")
            return
    print(f"{Num} is a Prime Number")
        
try:
    Num=int(input("Enter a positive Number:"))
    checkPrimeNum(Num)
except ValueError:
    print("Enter an Integer value!")