'''
Temperature Monitoring System 
Scenario: 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → daily temperature trend 
○ Bar chart → day-wise temperature 
○ Pie chart → proportion of high (>30) vs low temps 
○ Histogram → temperature frequency 
○ Scatter plot → day index vs temperature
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

temps=np.array([28, 30, 32, 35, 33, 31, 29]) 
days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df=pd.DataFrame({"Days":days,"Temperature":temps})
print(df)

plt.figure(figsize=(16,8))

#Line graph → daily temperature trend
plt.subplot(231)
plt.plot(df["Days"],df["Temperature"],marker='o')
plt.title("Daily temperature trend")
plt.xlabel("Days")
plt.ylabel("Temperature")

#Bar chart → day-wise temperature
plt.subplot(232)
plt.bar(df["Days"],df["Temperature"],color="black",width=0.4)
plt.title("Day-wise temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")

#Pie chart → proportion of high (>30) vs low temps
high_temp=(df["Temperature"]>30).sum()
low_temp=(df["Temperature"]<=30).sum()
explode=(0.08,0)
plt.subplot(233)
plt.pie([high_temp,low_temp],explode=explode,labels=["High Temperature","Low Temperature"],autopct="%1.1f%%",shadow=True,startangle=90)
plt.title("High vs low temperature")

#Histogram → temperature frequency
plt.subplot(234)
plt.hist(df["Temperature"],bins=6,histtype='bar',rwidth=0.5)
plt.title("Temperature frequency")
plt.xlabel("Days")
plt.ylabel("Temperature")

#Scatter plot → day index vs temperature
plt.subplot(235)
plt.scatter(df.index,df["Temperature"])
plt.title("Index vs Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.xticks(df.index,df["Days"])

plt.tight_layout()
plt.show()