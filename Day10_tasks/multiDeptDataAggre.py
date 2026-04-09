'''
Multi-Department Data Aggregation
A company collects employee counts from two branches.
Branch A:
[[10, 20],
[30, 40]]
Branch B:
[[5, 15],
[25, 35]]
Scenario:
● Combine the two matrices.
● Calculate the total employees across all departments.
● Print the combined matrix and total.
'''
from numpy import *

BranchA=array([[10,20],[30,40]])
BranchB=array([[5,15],[25,35]])

#branch=concatenate((BranchA,BranchB))
branch=BranchA+BranchB
total_emp=branch.sum()
print("Combined matrix:\n",branch)
print("Total employess across all departments:",total_emp)