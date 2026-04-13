'''
Temperature Alert System
Temperatures recorded in a city:
temps = np.array([28, 32, 35, 31, 29, 40, 38])
Task:
● Identify days where temperature is greater than 30.
● Return their indices.
'''
import numpy as np

temps=np.array([28, 32, 35, 31, 29, 40, 38])

t=np.where(temps>30)

print("Indices of temperatures, where temperature is greater than 30:\n",t)
