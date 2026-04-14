'''
Row Filtering + Aggregation
A dataset:
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
Task:
● Convert to DataFrame with columns "Sales", "Profit"
● Filter rows where Sales > 100
● Find average Profit of filtered row
'''
import pandas as pd
import numpy as np

arr=np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])

df=pd.DataFrame(arr,columns=["Sales","Profit"])

filtered_df=df[df["Sales"]>100]
avg=filtered_df["Profit"].mean()

print(df)
print(f"Filtered DataFrame:\n{filtered_df}")
print("Average Profit:",avg)