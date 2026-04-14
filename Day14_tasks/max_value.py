'''
Find Maximum Value
A dataset:
arr = np.array([12, 45, 22, 67, 34])
Task:
● Convert to Pandas Series
● Find the maximum value
'''
import numpy as np
import pandas as pd

arr=np.array([12, 45, 22, 67, 34])
arr_series=pd.Series(arr)
max_value=arr_series.max()

print("Array:",arr)
print(f"Series:\n{arr_series}")
print("Maximum value:",max_value)