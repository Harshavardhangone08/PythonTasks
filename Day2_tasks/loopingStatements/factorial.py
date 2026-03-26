# Write a program to calculate the factorial of a number using a loop.
# math.factorial() function

Num=int(input("Enter a number:"))
N=Num
fact=1
while(N>0):
    fact=fact*N
    N-=1
print("Factorial of {} = {}".format(Num,fact))
    