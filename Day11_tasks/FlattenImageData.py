'''
Reshape and Flatten Image Data
Scenario:
An image is stored as a 2 × 3 matrix:
[[1,2,3],
[4,5,6]]
Task:
1. Convert it into a NumPy array.
2. Flatten the array into 1-D format.
3. Print the flattened array
'''
import numpy as np

image=[[1,2,3],[4,5,6]]
image=np.array(image)
print("Image 2x3 matrix:\n",image)

image_1D=image.reshape(-1)

print("Flattened Array(1D):\n",image_1D)