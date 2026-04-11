'''
Filter Positive Even Numbers from Dataset
Scenario:
A dataset contains mixed values:
arr = [-5, 10, 15, -2, 20, 25, 30]
Task:
● Convert to NumPy array.
● Filter values that are:
○ Positive
○ Even
'''
import numpy as np

arr=[-5, 10, 15, -2, 20, 25, 30]
arr=np.array(arr)
print("Array:",arr)
#filter_arr=[]

filter_arr=(arr>0) & (arr%2==0)

even_arr=arr[filter_arr]
print("Array of positive even Numbers:",even_arr)
