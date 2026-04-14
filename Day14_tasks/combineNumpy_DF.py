'''
Combine NumPy Arrays into DataFrame
Two arrays:
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
Task:
● Create a DataFrame with columns "Name" and "Marks"
● Filter students with marks above 75
'''
import numpy as np
import pandas as pd

names=np.array(["A", "B", "C"])
marks=np.array([80, 90, 70])

Students=pd.DataFrame({"Name":names,"Marks":marks})
print(f"Student Data:\n{Students}")

Stu=Students[Students["Marks"]>75]
print("Filtered student data(Marks>75):")
print(Stu)