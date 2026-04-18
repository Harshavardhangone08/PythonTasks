'''
Employee Salary Insights 
Scenario: 
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
Task: 
● Convert into DataFrame 
● Plot: 
○ Line graph → salary trend 
○ Bar chart → department-wise salary comparison 
○ Pie chart → department distribution 
○ Histogram → salary distribution 
○ Scatter plot → index vs salary 
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

salaries=np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments=["HR", "IT", "HR", "IT", "Sales", "Sales"]

df=pd.DataFrame({"Department":departments,"Salaries":salaries})
print(df)

plt.figure(figsize=(15,10))

#Line graph salary trend
plt.subplot(231)
plt.plot(df["Department"],df["Salaries"],marker='o')
plt.title("Salary trend")
plt.xlabel("Departments")
plt.ylabel("Salaries")

#Bar chart → department-wise salary comparison
plt.subplot(232)
plt.bar(df["Department"],df["Salaries"],color="black",width=0.4)
plt.title("Department-wise salary comparison")
plt.xlabel("Departments")
plt.ylabel("Salaries")

#Pie chart → department distribution
dept_counts=df["Department"].value_counts()
plt.subplot(233)
plt.pie(dept_counts,labels=dept_counts.index,autopct="%1.1f%%",shadow=True,startangle=90)
plt.axis('equal')
plt.title("Department Distribution")

#Histogram → salary distribution
plt.subplot(234)
plt.hist(df["Salaries"],bins=5,histtype='bar',rwidth=0.8)
plt.title("Salary distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

#Scatter plot → index vs salary
plt.subplot(235)
plt.scatter(df.index,df["Salaries"])
plt.title("Index vs Salary")
plt.xlabel("Department Index")
plt.ylabel("Salary")

plt.tight_layout()
plt.show()