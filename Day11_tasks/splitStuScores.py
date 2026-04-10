'''
Splitting Student Scores Across Servers
A dataset:
[50, 60, 70, 80, 90, 100, 110, 120]
Scenario:
A distributed system needs to divide this data among 4 servers.
Task:
● Convert to NumPy array.
● Split the array into 4 equal parts using array_split().
'''
import numpy as np

scores=[50,60,70,80,90,100,110,120]
scores=np.array(scores)

print("Student Scores:",scores)
print()
print("Student scores after dividing among 4 servers:")
print(np.array_split(scores,4))