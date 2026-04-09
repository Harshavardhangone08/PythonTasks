'''
Matrix Transformation in Image Processing
An image processing system stores pixel intensity values in a matrix.
Scenario:
[[1, 2],
[3, 4]]
Task:
● Create a NumPy array for this matrix.
● Find its transpose.
● Print both matrices.
'''
import numpy as np

matrix=np.array([[1,2],[3,4]])
trans_matrix=matrix.transpose()
print("Matrix before Transpose:\n",matrix)
print("Matrix after Transpose:\n",trans_matrix)