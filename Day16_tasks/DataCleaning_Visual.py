'''
Data Cleaning + Visualization 
Scenario: 
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
Task: 
1. Convert to Pandas Series 
2. Replace NaN with mean 
3. Plot: 
○ Line graph of cleaned data 
○ Bar chart of values > average
'''

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data=np.array([100, np.nan, 200, 150, np.nan, 300]) 
S_data=pd.Series(data)
print(f"Original Series:\n{S_data}")
m=S_data.mean()
S_data=S_data.fillna(m)
print("Updated Series:")
print(S_data)

avg_data=S_data[S_data>m]
print(f"Values greater than average:\n{avg_data}")

plt.figure(figsize=(9,4))

plt.subplot(131)
plt.plot(S_data,linewidth=2)
plt.title("Line Graph")
plt.xlabel("Index")
plt.ylabel("Values")

plt.subplot(133)
plt.bar(avg_data.index,avg_data.values,width=0.5)
plt.title("Bar graph")
plt.xlabel("Index")
plt.ylabel("Values")
plt.show()