'''
Create a Python module named calculator.py that contains functions to perform:
● Addition
● Subtraction
● Multiplication
● Division
'''

#Addition (Multiple numbers)

def add(*numbers_add):
    val=0
    for num in numbers_add:
        val+=num
    return val
# print("Sum:",add(2,3,5))

# Substraction (Difference between two numbers)

def sub(a,b):
   return a-b
# print("Diff:",sub(5,10))

#Multiplication (Multiple numbers)

def multi(*numbers_multi):
    val=1
    for num in numbers_multi:
        val=val*num
    return val
#print("Multiplication:",multi(2,5,4))

# Division (Two numbers)

def div(a,b):
    return f"{a/b:.2f}"
#print("Division:",div(83,3))

