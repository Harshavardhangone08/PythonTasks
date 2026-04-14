'''
Filter Values Using Condition
A dataset:
arr = np.array([10, 25, 30, 15, 40])
Task:
● Convert to Pandas Series
● Filter values greater than 20
'''
import numpy as np
import pandas as pd

arr = np.array([10, 25, 30, 15, 40])

arr_s=pd.Series(arr)
print(arr_s)

Filtered_arr=arr_s[arr_s>20]
print(f"Filtered Array(>20):\n{Filtered_arr}")

