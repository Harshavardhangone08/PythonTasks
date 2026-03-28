# Write a recursive function to find the nth Fibonacci number.

def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

Num=int(input("Enter a positive number:"))

for i in range(Num):
     print(fibo(i),end=" ")