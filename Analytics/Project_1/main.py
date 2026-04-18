import pandas as pd
import matplotlib.pyplot as plt

#Load CSV file into pandas library
df=pd.read_csv('railway_guages.csv')
print(df.head())

#Year having maximum installations
max_install=df.iloc[[df["Total"].idxmax()]]
print(max_install)

#plot the graph
df=df.drop('Total',axis=1)
ax=df.plot(x="Year",kind='bar')
plt.xticks(rotation=70)
plt.xlabel("Year")
plt.ylabel("Total")
plt.title("Guages:Number of railway tracks installed per year")
plt.savefig('rail_guage.png')
plt.show()