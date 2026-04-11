'''
Boolean Masking for Salary Analysis
Scenario:
Employee salaries:
[25000, 40000, 15000, 50000, 30000]
Task:
● Filter salaries above 30000.
● Count how many employees satisfy this condition
'''

import numpy as np

salaries=np.array([25000, 40000, 15000, 50000, 30000])
print(salaries)

filter_arr=salaries>30000
sal=salaries[filter_arr]
#print("Salaries more than 30000:",sal)
print("Employees with salary more than 30000:",sal.size) # we can also use 'len(sal)'