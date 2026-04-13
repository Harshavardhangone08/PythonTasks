'''
Reshape & Row Averages
A dataset:
data = np.arange(1, 13)
Task:
● Reshape it into a 3×4 matrix
● Compute average of each row
'''
import numpy as np

data = np.arange(1, 13)
print(data)

data_2=data.reshape(3,4)
print("3x4 Matrix:\n",data_2)

data_avg=np.mean(data_2,axis=1)
print("Average of each row:",data_avg)