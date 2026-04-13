'''
Sales Threshold Filtering
You are given monthly sales:
sales = np.array([12000, 18000, 9000, 22000, 15000, 30000])
Task:
● Filter all sales values greater than the average sales
● Return the filtered array.
'''
import numpy as np

sales=np.array([12000, 18000, 9000, 22000, 15000, 30000])
avg=sum(sales)/len(sales)
filter_arr=sales>avg
filtered_sales=sales[filter_arr]
print(f"Average of sales:{avg:.2f}")
print("Sales values that are greater than the average sales:\n",filtered_sales)