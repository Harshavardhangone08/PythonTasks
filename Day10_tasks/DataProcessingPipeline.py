'''
Data Processing Pipeline
A data pipeline receives the following array:
[12, 7, 25, 3, 18, 10]
Scenario:
1. Convert the list into a NumPy array.
2. Sort the array.
3. Split the sorted array into two equal parts.
4. Calculate the sum of each part.
Output:
● Sorted array
● Two split arrays
● Sum of each part
'''
import numpy as np

data=[12,7,25,3,18,10]
data=np.array(data)

sorted_data=np.sort(data)
split_data=np.array_split(sorted_data,2)

print("Sorted array:\n",sorted_data)
print("Array after splitting into 2 equal parts:\n",split_data)
print("Sum of each part:")
print(f"{split_data[0].sum()} {split_data[1].sum()}")