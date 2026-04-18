'''
Monthly Sales Analysis 
Scenario: 
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → month-wise comparison 
○ Pie chart → contribution of each month 
○ Histogram → frequency of sales values 
○ Scatter plot → month index vs sales 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df=pd.DataFrame({"Month":months,"Sales":sales})
print(df)

plt.figure(figsize=(15,8))

#Line graph sales trend
plt.subplot(231)
plt.plot(df["Month"],df["Sales"],marker='o')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

#Bar chart month-wise comparison
plt.subplot(232)
plt.bar(df["Month"],df["Sales"])
plt.title("Month-wise Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")

#Pie chart contribution of each month
plt.subplot(233)
plt.pie(df["Sales"],labels=df["Month"],autopct='%1.1f%%',shadow=True,startangle=30)
#plt.axis('equal')
plt.title("Sales Contribution")

#Histogram frequency of sales values
plt.subplot(234)
plt.hist(df["Sales"],bins=5,histtype="bar",rwidth=0.8)
plt.title("Sales Frequency Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

#Scatter plot month index vs sales
plt.subplot(235)
plt.scatter(df.index, df["Sales"])
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.xticks(df.index, df["Month"])

plt.tight_layout()
plt.show()