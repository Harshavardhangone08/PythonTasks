'''
Write a Python program that generates 20 random numbers between 1 and 200 using
the random module and store them in a list.
Then using the math module, compute and display:
● Maximum value
● Minimum value
● Square root of the maximum number
● Logarithm of the minimum number
'''
from random import randint
from math import *

def m_module(li):
    ma=max(li)
    mi=min(li)
    print(f"Maximum value in the list:{ma}")
    print(f"Minimum value in the list:{mi}")
    print(f"Square root of the maximum number:{sqrt(ma):.2f}")
    print(f"Logarithm of the minimum number:{log(mi):.2f}")

li=[]
for i in range(20):
    li.append(randint(1,200))
    
print("List:",li)

m_module(li)

    

