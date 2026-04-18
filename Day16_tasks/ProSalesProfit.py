'''
Product Sales & Profit Analysis 
Scenario: 
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → product vs sales 
○ Pie chart → sales contribution 
○ Histogram → profit distribution 
○ Scatter plot → sales vs profit
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"]

df=pd.DataFrame({"Products":products,"Sales":sales,"Profit":profit})
print(df)

plt.figure(figsize=(16,8))

#Line graph → sales trend
plt.subplot(231)
plt.plot(df["Products"],df["Sales"],marker='o')
plt.title("Sales trend")
plt.xlabel("Products")
plt.ylabel("Sales")

#Bar chart → product vs sales
plt.subplot(232)
plt.bar(df["Products"],df["Sales"],color="black",width=0.5)
plt.title("Product vs Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

#Pie chart → sales contribution
plt.subplot(233)
explode=(0,0,0,0.1,0)
plt.pie(df["Sales"],explode=explode,labels=df["Products"],autopct="%1.1f%%",shadow=True,startangle=90)
plt.axis('equal')
plt.title("Sales contribution")

#Histogram → profit distribution
plt.subplot(234)
plt.hist(df["Profit"],bins=4,histtype='bar',rwidth=0.8)
plt.title("Profit distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")

#Scatter plot → sales vs profit
plt.subplot(235)
plt.scatter(df["Sales"],df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()
