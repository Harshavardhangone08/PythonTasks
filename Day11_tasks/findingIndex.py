'''
Find Indexes of Specific Value
A quality check system stores product defect codes:
[2, 4, 1, 4, 3, 4, 5]
Task:
● Find the indexes where value = 4 using NumPy searching.
'''
import numpy as np

defectCodes=np.array([2,4,1,4,3,4,5])

index=np.where(defectCodes==4)
print(f"Indexes where value is 4:{index}")