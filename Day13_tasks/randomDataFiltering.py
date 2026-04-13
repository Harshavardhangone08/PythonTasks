'''
Random Data & Filtering
Generate random numbers:
nums = np.random.randint(1, 100, 10)
Task:
● Filter values that are divisible by 5
● Return sorted result
'''
import numpy as np

nums=np.random.randint(1, 100, 10)
print(nums)

filter_arr=nums%5==0
nd_5=nums[filter_arr]
nd_5=np.sort(nd_5)
print("Numbers divisible by 5 from the array(sorted):",nd_5)