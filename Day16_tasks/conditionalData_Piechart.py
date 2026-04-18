'''
Pie Chart with Conditional Data 
Scenario: 
scores = np.array([40, 60, 80, 30, 90]) 
Task: 
● Categorize into: 
○ Pass (>50) 
○ Fail (<=50) 
● Count using NumPy/Pandas 
● Plot pie chart for Pass vs Fail
'''
import numpy as np
from matplotlib import pyplot as plt

scores = np.array([40, 60, 80, 30, 90]) 
Ps=scores[scores>50]
fail=scores[scores<=50]
print("Passed Students:",Ps)
print("Failed Students:",fail)
count=[len(Ps),len(fail)]
status=["Pass","Fail"]

#fig1,ax1=plt.subplots()

plt.pie(count,labels=status,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()
