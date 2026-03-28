# write another Python program that imports this module and performs calculations
# based on user input.

import calculator as cal

n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))

print("Arthimetic operations:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

user_input=int(input("Enter your choice(1-4):"))

if user_input==1:
   print("Addition:",cal.add(n1,n2))
   
elif user_input==2:
   print("Substraction:",cal.sub(n1,n2))

elif user_input==3:
   print("Multiplication:",cal.multi(n1,n2))

elif user_input==4:
   print("Division:",cal.div(n1,n2))

else:
    print("Invalid input!")
