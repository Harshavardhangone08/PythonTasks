'''
Check Data Type of Inventory Values
A warehouse stores product quantities:
[10, 20, 30, 40]
Task:
● Convert it into a NumPy array.
● Print the data type (dtype) of the array.
'''
import numpy as np

Products=[10,20,30,40]
Products=np.array(Products)
print(f"Type of array: {Products.dtype}")