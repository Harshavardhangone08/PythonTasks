'''
Student Marks Analysis (NumPy → Pandas)
Marks data:
arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])
Task:
● Convert into DataFrame with columns "Math", "Science"
● Add a new column Total
● Find student with highest total
'''
import numpy as np
import pandas as pd

arr = np.array([
[80, 90],
[70, 60],
[85, 95]
])

Marks=pd.DataFrame(arr,columns=["Math","Science"])
print(f"Marks Data:\n{Marks}")

Marks["Total"]=Marks["Math"]+Marks["Science"]
print(f"Marks Data after adding total:\n{Marks}")

Highest=Marks.loc[Marks["Total"].idxmax()]

print(f"Student with Highest total:\n{Highest}")