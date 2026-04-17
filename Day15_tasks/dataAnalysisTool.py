'''
Data Analysis Tool (NumPy + Pandas) 
Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results 
'''

from numpy import random
import pandas as pd

marks=random.randint(30,100,5)
print("Marks generated randomly:",marks)
df=pd.DataFrame(marks,columns=["Marks"])
df["Status"]=df["Marks"].apply(lambda x:"Pass" if x>=50 else "Fail")

df_status=df[df["Status"]=="Pass"]
df_mean=df_status["Marks"].mean()

print(f"Original Data Frame:\n{df}")
print(f"Passed students:\n{df_status}")
print(f"Average of Passed students:",df_mean)