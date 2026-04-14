'''
Data Alignment Issue in Series Addition
Two Series:
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
Task:
● Add both Series
● Explain why some values become NaN
● Replace NaN with 0 and compute final result
'''
import pandas as pd

S1=pd.Series([10,20,30],index=["a","b","c"])
S2=pd.Series([5,15,20],index=["b","c","d"])

S=S1+S2
print(f"After adding both the series:\n{S}")
print("a and d becomes NaN because the indexes are not common in S1 and S2, so we cannot add them.")

S=S.fillna(0) # replaces Nan with 0
print()
print(f"Series after replacing Nan with 0:\n{S}")
print(f"Final Result:{sum(S)}")