# Write a Python program that imports the package and uses functions from both modules

from utilities import math_operations , string_operations

print("1.Math operations")
print("2.String operations")
choice=int(input("Enter your choice(1/2):"))

if choice==1:
   n1=int(input("Enter a number:"))
   n2=int(input("Enter a number:"))
   n3=int(input("Enter a number:"))

   print("Addition:",math_operations.addition(n1,n2,n3))

   print("Multiplication:",math_operations.multiplication(n1,n2,n3))

elif choice==2:
    String=input("Enter a string:")
    
    print("String Uppercase:",string_operations.toUppercase(String))

    print("Count characters in string:",string_operations.countChar(String))

else:
    print("INVALID CHOICE!")

