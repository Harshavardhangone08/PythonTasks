'''
Missing Data Handling (NumPy + Pandas)
A dataset:
arr = np.array([10, np.nan, 30, np.nan, 50])
Task:
● Convert to Pandas Series
● Replace NaN values with the mean of the Series
● Print updated data
'''
import numpy as np
import pandas as pd

arr=np.array([10, np.nan, 30, np.nan, 50])

arr_s=pd.Series(arr)
m=arr_s.mean()
updatedSeries=arr_s.fillna(m)

print(arr_s)
print("Mean:",m)
print("Updated Series:")
print(updatedSeries)