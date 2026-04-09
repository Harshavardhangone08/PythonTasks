'''
Store Sales Comparison
Two stores record daily sales for 3 days.
Scenario:
Store A = [200, 250, 300]
Store B = [180, 270, 310]
Task:
● Store them in NumPy arrays.
● Find the daily difference in sales between the two stores.
● Print the resulting array.
'''
import numpy as np

StoreA=np.array([200,250,300])
StoreB=np.array([180,270,310])

daily_diff=StoreA-StoreB

print("Daily difference in sales between the two stores:\n",daily_diff)
