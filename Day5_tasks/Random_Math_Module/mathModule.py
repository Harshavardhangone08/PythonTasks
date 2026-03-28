# Write a Python program using the math module to calculate and display the square root,
# floor value, and ceiling value of a number entered by the user.

from math import *

def m_module(a):
    print(f"Square root of {a}: {sqrt(a):.2f}")
    print(f"Floor value of {a}: {floor(a)}")
    print(f"Ceiling value of {a}: {ceil(a)}")

Num=float(input("Enter a number:"))
m_module(Num)