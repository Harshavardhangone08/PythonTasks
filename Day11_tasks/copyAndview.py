'''
Copy vs View Behavior in Data Processing
Scenario:
A dataset:
[10, 20, 30, 40]
Task:
● Create a copy of the array.
● Modify the original array.
● Show that the copy does not change.
● Repeat using view() and observe the difference.
'''
import numpy as np

data=np.array([10,20,30,40])
print("Original Data:",data)
data_copy=data.copy() #creating a copy of the array 
data_view=data.view() #crating a view of the array

data[1]=25            # modifying the original array
print("Original Data after modification",data)

print()
print("Copy of original data:",data_copy)
print("Data in copied array doesnot change after modifying the original data!\n")

print("View of original data:",data_view)
print("If we use View function the data will be changed according to the original data modifications")
