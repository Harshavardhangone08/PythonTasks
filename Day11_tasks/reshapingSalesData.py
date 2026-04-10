'''
Reshaping Sales Data
A company stores monthly sales data:
[10,20,30,40,50,60,70,80,90,100,110,120]
Scenario:
You need to display the data as 4 months × 3 products matrix.
Task:
● Convert the list to NumPy array.
● Reshape it into a 4 × 3 array.
'''
import numpy as np

sales=[10,20,30,40,50,60,70,80,90,100,110,120]
sales=np.array(sales)

print("4 months × 3 products matrix:")
newSales=sales.reshape(4,3)

print(newSales)