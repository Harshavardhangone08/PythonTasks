'''
Multi-Line Graph for Sales Comparison 
Scenario: 
data = { 
"Month": ["Jan", "Feb", "Mar"], 
"Store_A": [100, 150, 200], 
"Store_B": [90, 140, 210] 
} 
Task: 
● Create DataFrame 
● Plot two line graphs on same plot 
● Add legend 
'''
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

data = { 
"Month": ["Jan", "Feb", "Mar"], 
"Store_A": [100, 150, 200], 
"Store_B": [90, 140, 210] 
} 

df=pd.DataFrame(data)
print(df)

plt.plot(df["Month"],df["Store_A"],'r',label="Store A",linewidth=2)
plt.plot(df["Month"],df["Store_B"],'k',label="Store B",linewidth=2)
plt.title("Sales Comparison")
#plt.figure(figsize=(10,4))

plt.ylabel("Sales")
plt.xlabel("Month")
plt.legend()
plt.grid(True,color='k')
plt.tight_layout()
plt.show()