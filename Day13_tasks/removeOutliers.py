'''
Remove Outliers
Given data:
values = np.array([10, 12, 15, 18, 100, 14, 13])
Task:
● Compute the mean and standard deviation
● Remove values that are more than 2 standard deviations from the mean
'''
import numpy as np

values=np.array([10, 12, 15, 18, 100, 14, 13])

mean_values=np.mean(values)
S_D=np.std(values)
print("Mean:",mean_values)
print(f"Standard Deviation:{S_D:.2f}")
filtered = values[np.abs(values - mean_values)<=2*S_D]

print("Filtered Data:", filtered)