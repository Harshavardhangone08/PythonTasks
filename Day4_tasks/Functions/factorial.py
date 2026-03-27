# Write a function that returns the factorial of a number.

def fact(n):
   f=1
   while(n>0):
      f*=n
      n=n-1
   return f

num=int(input("Enter a number:"))
facto_num=fact(num)
print(f"Factorial of {num}:{facto_num}",)