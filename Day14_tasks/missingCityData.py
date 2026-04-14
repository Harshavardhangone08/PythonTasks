'''
Missing City Data (NaN Handling)
A dataset contains city populations:
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
Scenario:
You want data for:
["Delhi", "Chennai", "Bangalore"]
Task:
● Create a Series with the above index
● Identify which cities have missing values (NaN)
'''
import pandas as pd

cities={"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}

data=["Delhi","Chennai","Bangalore"]
my_cities=pd.Series(cities,index=data)
print(my_cities)