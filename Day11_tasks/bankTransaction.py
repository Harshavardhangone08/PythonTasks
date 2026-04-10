'''
Bank Transaction Storage
A bank stores the transaction amounts of a customer in a list:
[1200, 500, 800, 1500]
Scenario:
● Convert the list into a NumPy array.
● Print the type of the object.
● Verify that it is a NumPy ndarray.
'''
import numpy as np

Trans=np.array([1200,500,800,1500])
print("Transaction Amounts of a customer:",Trans)

print("Verifying that the array is a Numpy ndarray or not") # type of the object
print(type(Trans))

