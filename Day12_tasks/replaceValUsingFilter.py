'''
Replace Values Using Filtering
Scenario:
A dataset contains:
[5, 12, 18, 7, 25, 30]
Task:
● Replace all values greater than 15 with 0 using NumPy filtering
'''

import numpy as np

data=np.array([5, 12, 18, 7, 25, 30])
print("Array:",data)
data[data>15]=0
print("Array after filtering:",data)