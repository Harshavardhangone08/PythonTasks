'''
Complex DataFrame Transformation
A DataFrame:
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})
Scenario:
● Students scoring below 50 failed
Task:
1. Create a column Status ("Pass"/"Fail")
2. Filter only passed students
3. Calculate average marks of passed student
'''
import pandas as pd

df=pd.DataFrame({"Name":['A','B','C','D'],"Marks":[50, 80, 30, 90]})
df["Status"]=df["Marks"].apply(lambda x:"Pass" if x>=50 else "Fail")

print(f"Student Database:\n{df}")
df_pass=df[df["Status"]=="Pass"]

avg=df_pass["Marks"].mean()

print(f"Passed Students:\n{df_pass}")
print(f"Average marks of passed students:{avg:.2f}")