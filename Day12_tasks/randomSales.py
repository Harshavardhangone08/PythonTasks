'''
Random Sales Simulation
Scenario:
A company wants to simulate 10 days of sales (range 100–500).
Task:
● Generate random integers using NumPy.
● Print the array.
● Find the average sales.
'''
from numpy import random

arr=random.randint(100,500,size=10)

print(arr)

avg=sum(arr)/10
print("Average:",avg)