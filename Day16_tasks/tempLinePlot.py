'''
Temperature Trend Line Plot 
Scenario: 
Daily temperatures: 
temps = np.array([28, 30, 32, 31, 29]) 
Task: 
● Convert into Pandas Series 
● Plot a line graph 
● Add title and grid 
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])
df=pd.DataFrame(temps,columns=["Temp"])
print(df)

plt.plot(temps)
plt.title("Temperature Trend")
plt.grid(True,color='c')
plt.show()