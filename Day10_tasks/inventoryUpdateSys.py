'''
Inventory Update System
A warehouse has an inventory stored in a matrix.
[[10, 15],
[20, 25]]
Scenario:
A new shipment increases every item quantity by 2 units.
Task:
● Add 2 to every element using NumPy.
● Print the updated inventory.
'''
from numpy import array

inventory=array([[10,15],[20,25]])

inventory_2=inventory+2
print("Updated inventory:\n",inventory_2)