'''
Combined Visualization Dashboard 
Scenario: 
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph (trend) 
○ Bar chart (comparison) 
○ Pie chart (distribution) 
● Show all in single figure (subplots)
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"]

df=pd.DataFrame({"Product":products,"Sales":sales})
print(df)

plt.figure(figsize=(10,5))

plt.subplot(131)
plt.plot(df["Product"],df["Sales"])
plt.title("Trends")
plt.subplot(132)
plt.bar(df["Product"],df["Sales"])
plt.title("Comaprison")
plt.subplot(133)
explode=(0,0,0,0.1)
plt.pie(sales,explode=explode,labels=products,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.title("Distribution")

plt.suptitle("Product Sales Dashboard")
plt.show()
