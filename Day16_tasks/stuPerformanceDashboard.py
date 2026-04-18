'''
Student Performance Dashboard 
Scenario: 
A school records marks of students in one subject: 
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
Task: 
● Convert to Pandas DataFrame 
● Plot: 
○ Line graph → trend of marks 
○ Bar chart → student vs marks 
○ Pie chart → Pass (>50) vs Fail 
○ Histogram → distribution of marks 
○ Scatter plot → index vs marks 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 

df=pd.DataFrame({"Students":students,"Marks":marks})
print(df)

pass_count=(df["Marks"]>50).sum()
fail_count=(df["Marks"]<=50).sum()

print(pass_count)
print(fail_count)

plt.figure(figsize=(15,8))

#Line Graph trend of marks
plt.subplot(231)
plt.plot(df["Students"],df["Marks"],)
plt.title("Trend of marks")
plt.xlabel("Students")
plt.ylabel("Marks")

#Bar chart student vs marks
plt.subplot(232)
plt.bar(df["Students"],df["Marks"],width=0.4)
plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

#Pie chart Pass (>50) vs Fail
plt.subplot(233)
explode=(0.08,0)
plt.pie([pass_count,fail_count],explode=explode,labels=["Pass","Fail"],shadow=True,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title("Pass vs Fail")

#Histogram distribution of marks
plt.subplot(234)
plt.hist(df["Marks"],bins=5,histtype="bar",rwidth=0.6)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

#Scatter plot index vs marks
plt.subplot(235)
plt.scatter(range(len(df)),df["Marks"])
plt.title("Index vs Marks")
plt.xlabel("Students Index")
plt.ylabel("Marks")
plt.xticks(range(len(df)),df["Students"])

plt.tight_layout()
plt.show()