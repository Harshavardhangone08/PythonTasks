'''
Temperature Monitoring System
A weather station records temperatures for two days.
Scenario:
Day 1: [30, 32, 31]
Day 2: [29, 33, 34]
Task:
● Create a 2D NumPy array to store this data.
● Print the array.
● Find the total temperature recorded.
'''

import numpy as np

temp=np.array([[30,32,31],[29,33,34]])

print("Temperature for two days:\n",temp)

print("Total temperature:",temp.sum())

