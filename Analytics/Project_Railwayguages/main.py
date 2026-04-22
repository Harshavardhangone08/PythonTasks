# ==============================================================================
#  Project Title: Railway Gauge Data Analysis 
#  Analysing the railway gauge dataset using Numpy, Pandas and matplotlib
# ==============================================================================

#==============================================================================
#                  Importing the required libraries
#==============================================================================
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

'''
==================================================================================
                    Scenario 1: Basic Data Loading & Cleaning 
==================================================================================
You are given a CSV file containing railway gauge data. 
Tasks: 
1. Load the dataset into a Pandas DataFrame. 
2. Display the first 5 rows and column names. 
3. Check for missing values and replace them with 0. 
4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types. 
'''
# 1.1-Loading the Dataset into pandas dataframe
df=pd.read_csv("railway_guages_1.csv")

# 1.2-to display first 5 rows and column names
print("First 5 rows from the dataset:")
print(df.head())

#print(df.shape) to check for number of rows and columns 
# 1.3-checking for null values
print(f"Checking for NULL values:\n{df.isnull().sum()}")
df=df.fillna(0) #To replace missing values with '0'

# 1.4-Converting all gauge columns(Broad, Metre, Narrow, Total) to numeric types.
guage_cols=['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
df[guage_cols]=df[guage_cols].apply(pd.to_numeric,errors='coerce')
print(df)

'''
==================================================================================
                    Scenario 2: Simple Visualization 
==================================================================================
You want a quick understanding of total railway track growth. 
Tasks: 
1. Extract Year and Total columns. 
2. Plot a line graph showing Total tracks over years. 
3. Add: 
○ Title 
○ X and Y labels 
4. Identify whether the trend is increasing or decreasing.
'''
# 2.1 Extracting year and Total columns
df_YT=df[["Year","Total"]]

# 2.2-Plotting a line graph between Total and Years
plt.plot(df_YT['Year'],df_YT['Total'],marker='o')

# 2.3 Adding Title, xlabel and ylabel
plt.title("Total railway tracks over years")
plt.xlabel("Years")
plt.ylabel("Total tracks")
plt.xticks(rotation=75)
plt.savefig("Line_graph_YT.png")
plt.show()

# 2.4-Analysing the trend
first=df_YT["Total"].iloc[0]
last=df["Total"].iloc[-1] 
if last>first:
    trend="Increasing"
elif first>last:
    trend="Decreasing"
else:
    trend="No change"
print("Trend Analysis:")
print(f"First Year Total:{first}\nLast Year Total:{last}\nOverall trend:{trend}")

'''
==================================================================================
                    Scenario 3: Filtering + Bar Chart 
==================================================================================
You are asked to analyze modern railway expansion. 
Tasks: 
1. Filter the dataset for years after 2000. 
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge. 
3. Plot a grouped bar chart comparing all three gauges. 
4. Add legend and proper labels. 
5. Identify which gauge dominates in recent years. 
'''
# 3.1 filtering the dataset for years after 2000, Year = "2000-01"
df2=df.copy()  #copying the dataframe
df2["Year_start"]=df2["Year"].str[:4].astype(int)
df2=df2[df2["Year_start"]>2000]
print(f"Filtered dataframe:\n{df2}")

# 3.2 Select Broad Gauge, Metre Gauge, and Narrow Gauge
df2_Bargraph=df2[["Year","Broad Gauge","Metre Gauge","Narrow Gauge"]]

# 3.3 Plot a grouped bar chart comparing all three gauges
x=np.arange(len(df2_Bargraph["Year"]))
width=0.25
fig,ax=plt.subplots(figsize=(12,5))
ax.bar(x-width,df2_Bargraph["Broad Gauge"],label="Broad Gauge",color="black",width=width)
ax.bar(x,df2_Bargraph["Metre Gauge"],label="Metre Gauge",color="green",width=width)
ax.bar(x+width,df2_Bargraph["Narrow Gauge"],label="Narrow Gauge",color="blue",width=width)

# 3.4 Adding proper labels and legend function
plt.suptitle("Gauge wise Railway Tracks after 2000")
plt.xlabel("Year")
plt.ylabel("Track length")
plt.xticks(x,df2_Bargraph["Year"],rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("Bar_graph.png")
plt.show()

#3.5 Gauge dominates in recent years
recent=df2_Bargraph.tail()[["Broad Gauge","Metre Gauge","Narrow Gauge"]]
dominant=recent.mean().idxmax()
print("Dominant Guage:",dominant)

'''
==================================================================================
                    Scenario 4: Feature Engineering + Pie Chart 
==================================================================================
You want to analyze the contribution of each gauge type. 
Tasks: 
1. Calculate total sum of each gauge across all years. 
2. Create a new structure (Series/DataFrame) for totals. 
3. Plot a pie chart showing percentage contribution. 
4. Add percentage labels (autopct). 
5. Interpret which gauge contributes the most. 
'''
# 4.1 Total sum of each gauge across all years
broad_sum=df["Broad Gauge"].sum()
metre_sum=df["Metre Gauge"].sum()
narrow_sum=df["Narrow Gauge"].sum()

# 4.2 creating a series structure for totals
gauge_total=pd.Series({"Broad Gauge":broad_sum,"Metre Gauge":metre_sum,"Narrow Gauge":narrow_sum})
print("Total sum of each gauge across all years:")
print(gauge_total)

# 4.3, 4.4  Plotting a pie chart and adding percentage labels
plt.figure(figsize=(12,5))
plt.pie(gauge_total,labels=gauge_total.index,autopct='%1.1f%%',shadow=True,startangle=90)
plt.title("Percentage of Contribution of each Gauge")
plt.tight_layout()
plt.savefig("Pie_chart.jpg")
plt.show()

#4.5 Gauge that contribute the most
dominant_gauge=gauge_total.idxmax()
dominant_gauge_per=(gauge_total.max()/gauge_total.sum())*100
print(f"Guage with most contribution:{dominant_gauge}")
print(f"Contribution percentage:{dominant_gauge_per:.2f}")

'''
==================================================================================
               Scenario 5: Advanced Analysis + Multiple Graphs 
==================================================================================
You are asked to perform a complete analysis of railway trends. 
Tasks: 
1. Create new columns: 
○ % Broad Gauge 
○ % Metre Gauge 
○ % Narrow Gauge 
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks. 
3. Plot: 
○ Line graph for all gauges 
○ Stacked bar chart showing composition 
4. Highlight: 
○ Years with highest growth 
○ Decline in any gauge 
5. Provide a final conclusion: 
“Is the railway system shifting towards a single dominant gauge?” 
'''
#5.1 Creating new columns of Gauge percentage
df3=df.copy()  #Copying the dataframe, so that the original dataframe remains the same

# To calculate percentage p=(value/Total)*100  and round() funtion to roundoff the decimal value to 2 places
df3["% Broad Gauge"]=((df3["Broad Gauge"]/df3["Total"])*100).round(2)
df3["% Metre Gauge"]=((df3["Metre Gauge"]/df3["Total"])*100).round(2)
df3["% Narrow Gauge"]=((df3["Narrow Gauge"]/df3["Total"])*100).round(2)
print("Data Frame with updated percentage columns:")
print(df3[["Year","% Broad Gauge","% Metre Gauge","% Narrow Gauge"]].head())

#5.2 Using NumPy (np.diff) to calculate yearly growth of Total tracks
growth = np.diff(df3["Total"])

# Adding first year as NaN because diff gives one less value
df3["Total Growth"]=np.insert(growth.astype(float),0,0)
print("\nYearly Growth of Total Tracks:")
print(df3[["Year","Total","Total Growth"]].head())

# 5.3.1 Line graph for all gauges
plt.figure(figsize=(10, 5))
plt.plot(df3["Year"], df3["Broad Gauge"], label="Broad Gauge")
plt.plot(df3["Year"], df3["Metre Gauge"], label="Metre Gauge")
plt.plot(df3["Year"], df3["Narrow Gauge"], label="Narrow Gauge")
plt.title("Line Graph for All Gauges")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("All_gauges.png")
plt.show()

# 5.3.2 Stacked bar chart showing composition
plt.figure(figsize=(10, 5))
plt.bar(df3["Year"], df3["Broad Gauge"], label="Broad Gauge")
plt.bar(df3["Year"], df3["Metre Gauge"],bottom=df3["Broad Gauge"], label="Metre Gauge")   
plt.bar(df3["Year"], df3["Narrow Gauge"],bottom=df3["Broad Gauge"] + df3["Metre Gauge"],label="Narrow Gauge")
plt.title("Stacked Bar Chart of Gauge Composition")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig("stackedBarchart.png")
plt.show()

# 5.4.1 Highlighting highest growth year
max_growth=df3["Total Growth"].max()
max_growth_year=df3.loc[df3["Total Growth"].idxmax(), "Year"]
print(f"\nHighest Growth Year:{max_growth_year}\nGrowth Value:{max_growth}")

# 5.4.2 Checking decline in gauges
print("\nDecline in Gauges:")
for gauge in ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]:
    decline_years=df3[df3[gauge].diff() < 0]["Year"]
    print(f"{gauge} declined in years:")
    print(list(decline_years))
    
# 5.5 Final conclusion
start_bg=df3["% Broad Gauge"].iloc[0]
end_bg=df3["% Broad Gauge"].iloc[-1]
print("\nFinal Conclusion:")
if end_bg>start_bg:
    print("Yes, the railway system is shifting towards a single dominant gauge(Broad Gauge).")
else:
    print("No, there is no clear shift towards a single dominant gauge.")