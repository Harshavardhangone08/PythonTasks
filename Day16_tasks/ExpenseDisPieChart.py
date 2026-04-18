'''
Expense Distribution Pie Chart 
Scenario: 
Monthly expenses: 
expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"] 
Task: 
● Create a pie chart 
● Show percentage distribution 
'''
import numpy as np
import matplotlib.pyplot as plt

expenses = np.array([500, 300, 200]) 
Label=["Food", "Rent", "Travel"]
explode=(0.1,0,0)

fig1,ax1=plt.subplots()
ax1.pie(expenses,explode=explode,labels=Label,autopct='%1.1f%%',shadow=True,startangle=90) #(explode=explode)
ax1.axis('equal')
plt.show()
