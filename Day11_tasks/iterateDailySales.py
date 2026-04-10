'''
Iterate Through Daily Sales
Daily sales data:
[200, 300, 150, 400]
Task:
● Store it in a NumPy array.
● Iterate through the array and print each sale values
'''
import numpy as np

sales=np.array([200,300,150,400])
print("Daily sales data:")
for i in sales:
   print(i)

''' using built-in funtion nditer()

for i in np.nditer(sales):
    print(i)
'''