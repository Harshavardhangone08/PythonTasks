'''
Convert NumPy Array to Pandas Series
A dataset:
arr = np.array([10, 20, 30, 40])
Task:
● Convert this NumPy array into a Pandas Series
● Assign index labels: ["A", "B", "C", "D"]
'''
import numpy as np
import pandas as pd
arr=np.array([10, 20, 30, 40])
print("Array:",arr)

arr_series=pd.Series(arr,index=["A","B","C","D"])
print(f"Pandas Series:\n{arr_series}")

