'''
 Splitting Data for Parallel Processing
A dataset contains the following values:
[5, 10, 15, 20, 25, 30]
Scenario:
You want to distribute the data across 3 processors.
Task:
● Store the data in a NumPy array.
● Split it into 3 equal parts using NumPy.
'''
import numpy as np

data=[5,10,15,20,25,30]
data=np.array(data)
d=np.array_split(data,3)
print("Data after splitting into 3 equal parts:\n",d)