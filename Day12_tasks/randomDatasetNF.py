'''
Random Dataset Normalization + Filtering
Scenario:
● Generate 8 random float values between 0 and 1.
Task:
1. Normalize by multiplying with 100
2. Filter values greater than 50
3. Sort the filtered value
'''
import numpy as np

dataset=np.random.rand(8)
dataset=np.round(dataset,2) # used round() function to roundup the decimal value to 2 positions
print(dataset)
Norm_dataset=dataset*100 # Normalizing by multiplying with 100
print("After Normalization:")
print(Norm_dataset)
filter_arr=Norm_dataset>50

data=Norm_dataset[filter_arr]
print("Sorted values after Filtering:")
print(np.sort(data))