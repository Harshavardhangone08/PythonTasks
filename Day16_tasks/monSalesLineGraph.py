'''
1. Monthly Sales Line Graph 
Scenario: 
A shop records monthly sales: 
sales = np.array([100, 150, 200, 250, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May"] 
Task: 
● Convert data into a Pandas DataFrame 
● Plot a line graph 
● Label X-axis as months and Y-axis as sales
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sales=np.array([100, 150, 200, 250, 300])
months=["Jan", "Feb", "Mar", "Apr", "May"]


df=pd.DataFrame({"Month":months,"Sales":sales})
print(df)

plt.plot(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()