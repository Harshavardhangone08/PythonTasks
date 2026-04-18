'''
Filtered Bar Chart 
Scenario: 
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"] 
Task: 
● Convert to DataFrame 
● Filter students with marks > 50 
● Plot bar chart only for filtered students
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"]

df=pd.DataFrame({"Name":names,"Marks":marks})
print(df)
filtered_df=df[df["Marks"]>50]
print("Filtered DataFrame:")
print(filtered_df)

plt.bar(filtered_df["Name"],filtered_df["Marks"],width=0.4,color="green")
plt.title("Passed Students")
plt.xlabel("Student names")
plt.ylabel("Marks")
plt.show()