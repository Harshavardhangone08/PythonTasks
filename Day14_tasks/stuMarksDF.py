'''
Student Marks DataFrame Analysis
A DataFrame:
data = pd.DataFrame({
"Name": ["A", "B", "C"],
"Math": [80, 70, 60],
"Science": [90, 60, 70]
})
Task:
● Add a new column Total = Math + Science
● Find the student with the highest total marks
'''
import pandas as pd

data=pd.DataFrame({"Name":["A","B","C"],
                   "Math":[80,70,60],
                   "Science":[90,60,70]})
data["Total"]=data["Math"]+data["Science"]
print(data)

#max_marks=data[data["Total"]==data["Total"].max()]  using max method

max_marks=data.loc[data["Total"].idxmax()]

# loc[] retruns the complete row 
# idxmax() gives index of the max value

print("Top Student:")
print(max_marks)