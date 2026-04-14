'''
Adding and Updating Columns
A DataFrame:
df = pd.DataFrame({
"Price": [100, 200, 300]
})
Scenario:
● Add a column Discount = 10% of Price
● Add another column Final Price = Price - Discount
'''
import pandas as pd

df=pd.DataFrame({"Price":[100,200,300]})
df["Discount"]=df["Price"]*0.1
df["Final Price"]=df["Price"]-df["Discount"]
print(df)