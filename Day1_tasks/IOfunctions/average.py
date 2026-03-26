#program that takes three numbers as input and prints their average.
num1,num2,num3=map(int,input("Enter three numbers:").split())
avg=((num1+num2+num3))/3
print("Average of 3 numbers:",avg)