'''
Filter High Temperature Values
A weather station records temperatures:
[28, 31, 35, 27, 40, 22]
Scenario:
The system needs temperatures above 30°C.
Task:
● Filter the values greater than 30 using NumPy boolean filtering
'''

import numpy as np

temp=np.array([28,31,35,27,40,22])
filter_arr=[] #empty list

for t in temp:
    if t>30:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newTemp=temp[filter_arr]
#print(filter_arr)
print(newTemp)