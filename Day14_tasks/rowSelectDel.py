'''
Row Selection & Deletion
A DataFrame:
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
Task:
● Select row with index "y"
● Delete row "x"
● Print updated DataFrame
'''
import pandas as pd

df=pd.DataFrame({"A":[10,20,30],"B":[5,15,25]},index=['x','y','z'])

print(f"Values in Row 'y':\n{df.loc['y']}")

df=df.drop('x')
print()
print("Updated DataFrame Table(After deleting row 'x'):")
print(df)