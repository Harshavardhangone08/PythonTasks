'''
A company wants to organize its Python code using packages.
Create a package named utilities that contains two modules:
● math_operations.py (functions for addition and multiplication)
● string_operations.py (functions to convert string to uppercase and count
characters)
Write a Python program that imports the package and uses functions from both modules
'''
#Addition
def addition(*numbers):
    val=0
    for num in numbers:
        val+=num
    return val

#Multiplication
def multiplication(*numbers):
    val=1
    for num in numbers:
        val*=num
    return val
