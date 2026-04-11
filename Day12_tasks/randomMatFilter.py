''' 
Random Matrix and Condition Filtering
Scenario:
● Generate a 3×3 matrix of random numbers (0–50).
Task:
● Filter elements greater than 25.
● Print filtered values.
'''
from numpy import random

arr=random.randint(50,size=(3,3))
print(arr)
print()
filter_arr=arr>25

new_arr=arr[filter_arr]
print("Filtered array:")
print(new_arr)