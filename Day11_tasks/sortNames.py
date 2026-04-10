'''
Sorting Customer Names
A system stores customer names:
["Ravi", "Anil", "Sita", "John"]
Task:
● Convert it to a NumPy array.
● Sort the names alphabetically.
'''
import numpy as np

names=["Ravi","Anil","Sita","John"]
names=np.array(names)

print("Names before sorting:",names)
print(f"Names after sorting alphabetically: {np.sort(names)}")
