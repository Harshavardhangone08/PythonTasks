# ==============================================================================
#  Project Title: Scottish Hills Data Analysis 
#  Analysing the Scottish Hills dataset using Numpy, Pandas and matplotlib
# ==============================================================================

#===============================================================================
#                  Importing the required libraries
#===============================================================================
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
'''
===============================================================================
                Scenario 1: Data Loading & Basic Cleaning
===============================================================================
Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows 
○ Column names 
3. Check for missing values in: 
○ Height 
○ Region 
4. Fill missing values: 
○ Height → use mean 
○ Region → use mode 
5. Convert Height column to numeric if required. 
'''
#1.1 Load the dataset using Pandas.
df = pd.read_csv("scottish_hills.csv")

#1,2 Display first 5 rows and column names
print("(S1)First 5 rows:\n", df.head())
print("========================================================")
print("\n(S1)Column names:\n", df.columns)
print("========================================================")
# Clean column names (important)
df.columns = df.columns.str.strip().str.title()
# 3. Create Region column (if not available)
if "Region" not in df.columns:
    #print("\n(S1)Region column not found → Creating using Latitude & Longitude")
    # Midpoints
    lat_mid = df["Latitude"].median()
    lon_mid = df["Longitude"].median()
    # Function to assign region
    def assign_region(row):
        lat = row["Latitude"]
        lon = row["Longitude"]
        if lat >= lat_mid and lon >= lon_mid:
            return "North-East"
        elif lat >= lat_mid and lon < lon_mid:
            return "North-West"
        elif lat < lat_mid and lon >= lon_mid:
            return "South-East"
        else:
            return "South-West"

    # Apply function
    df["Region"] = df.apply(assign_region, axis=1)

print("Dataset after adding Region column:")
print(df)
# 4. Convert Height to numeric (before checking missing)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

#1.3. Check for missing values height and region 
print("\nMissing values:")
print(df[["Height", "Region"]].isnull().sum())
print("========================================================")

# 1.4. Handle missing values
df["Height"] = df["Height"].fillna(df["Height"].mean())
df["Region"] = df["Region"].fillna(df["Region"].mode()[0])

print("\n(S1)After handling missing values:")
print(df[["Height", "Region"]].head())
print("========================================================")

# 1.5. Convert Height to numeric (if needed)
df["Height"] = pd.to_numeric(df["Height"], errors="coerce")

print("\n(S1)Data types after conversion:")
print(df.dtypes)
print("========================================================")
print("========================================================")

'''
===============================================================================
                Scenario 2: Line Graph + Save 
===============================================================================
You want to see how heights vary. 
Tasks: 
1. Select: 
○ Hill Name 
○ Height 
2. Take first 10 rows only. 
3. Convert Height into a NumPy array. 
4. Plot a line graph: 
○ X-axis → index (0–9) 
○ Y-axis → Height 
5. Add title and labels. 
Save the graph: plt.savefig("hill_heights_line.png")
'''
# 2.1 Select required columns
data = df[["Hill Name", "Height"]]
print("\n(S2)Selecting required columns\n", data)
print("========================================================")
# 2.2 Take first 10 rows
data = data.head(10)
print("\n(s2)data\n", data)
print("========================================================")
print("========================================================")
# 2.3 Convert Height to NumPy array
heights = data["Height"].to_numpy()
 
# 2.4 Plot line graph
plt.figure(figsize=(10,6))
plt.plot(range(len(heights)), heights, marker='o')
# 2.5 Add title and labels
plt.title("Height Variation of First 10 Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.grid(True)
plt.tight_layout()
# 2.6 Save the graph
plt.savefig("Graphs/hill_heights_line.png")
# Show plot
plt.show()
'''
===============================================================================
                Scenario 3: Filtering + Bar Chart + Save 
===============================================================================
You want to analyze tall hills. 
Tasks: 
1. Filter hills where: 
○ Height > 900 
2. Count number of hills per Region. 
3. Select top regions. 
4. Convert results to NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → Region 
○ Y-axis → count 
6. Rotate labels for clarity. 
Save graph: plt.savefig("tall_hills_bar.png")
'''
# 3.1 Filter hills where Height > 900
tall_hills = df[df["Height"] > 900]
print("\n(S3)Tall_hills", tall_hills)
print("========================================================")
# 3.2 Count number of hills per Region
region_counts = tall_hills["Region"].value_counts()
print("\n(S3)region_counts\n", region_counts)
print("========================================================")
# 3.3 Select top regions (top 5 for clarity)
top_regions = region_counts.head()
print("\n(S3)top_regions\n", top_regions)
print("========================================================")
# 3.4 Convert results to NumPy arrays
regions = top_regions.index.to_numpy()
print(type(regions))
counts = top_regions.values
print(type(counts))
print("========================================================")
print("========================================================")
# 3.5 Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(regions, counts,width=0.5)
# Labels and title
plt.xlabel("Region")
plt.ylabel("Count")
plt.title("Bar Graph Of Top Regions with Tall Hills (>900)")
# 3.6 Rotate labels
plt.xticks(rotation=45)
plt.tight_layout()
# Save graph
plt.savefig("Graphs/tall_hills_bar.png")
plt.show()
'''
===============================================================================
                Scenario 4: Pie Chart (Region Distribution) + Save
=============================================================================== 
You want to see the distribution of hills. 
Tasks: 
1. Count the number of hills per Region. 
2. Select top 5 regions. 
3. Prepare labels and values. 
4. Plot a pie chart. 
5. Add percentage labels. 
Save graph: plt.savefig("region_distribution.png") 
'''
#4.1 Number of hills per region
Hills=df.groupby("Region")["Hill Name"].count().reset_index()
Hills.columns=["Region","Hills_count"]
print(f"Number of Hills per region:\n{Hills}")
#4.2 Top 5 regions
top_5=Hills.sort_values("Hills_count",ascending=False).head()
#4.3 Assigning labels and values
labels=top_5["Region"]
values=top_5["Hills_count"]
#4.4, 4.5, 4.6 - Pie chart
plt.figure(figsize=(10,6))
plt.pie(values,labels=labels,explode=(0.06,0,0,0),shadow=True,autopct='%1.1f%%',startangle=90)
plt.title("Top regions by Hill count")
plt.tight_layout()
plt.savefig("Graphs/region_distribution.png")
plt.show()
'''
Scenario 5: Advanced Analysis + Multiple Graphs  
You want deeper insights. 
Part 1: Feature Creation 
1. Create a new column: 
○ Height Category: 
■ Height >= 1000 → "Very High" 
■ 800–999 → "High" 
■ < 800 → "Moderate" 
Part 2: NumPy Usage 
2. Convert Height column to NumPy array. 
Calculate height differences using: 
np.diff() 
Part 3: Visualizations 
Line Graph 
4. Plot height trend for all hills. 
Stacked Bar Chart 
5. Show count of Height Category per Region. 
Histogram 
6. Plot distribution of Height. 
Part 4: Save All Graphs 
plt.savefig("height_trend.png") 
plt.savefig("height_category_stacked.png") 
plt.savefig("height_histogram.png") 
Part 5: Insights
● Which region has tallest hills 
● Which category is most common 
● Distribution pattern of heights 
'''
# Part 1: Feature Creation
def categorize_height(h):
    if h >= 1000:
        return "Very High"
    elif 800 <= h <= 999:
        return "High"
    else:
        return "Moderate"

df["Height Category"] = df["Height"].apply(categorize_height)
print(df[["Height", "Height Category"]].head())
print("========================================================")
# Part 2: NumPy Usage
height_array = df["Height"].to_numpy()
height_diff = np.diff(height_array)
print("\nHeight Differences:\n", height_diff)
print("========================================================")
# Part 3: Visualizations
# 📈 Line Graph (Height Trend)
plt.figure(figsize=(10, 6))
plt.plot(df.index, df["Height"], color='blue')
plt.title("Height Trend of All Hills")
plt.xlabel("Index")
plt.ylabel("Height")
plt.grid(True)
plt.savefig("Graphs/height_trend.png")
plt.show()

# 📊 Stacked Bar Chart (Category per Region)
cat_region = pd.crosstab(df["Region"], df["Height Category"])
cat_region.plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Height Category per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.savefig("Graphs/height_category_stacked.png")
plt.show()

# 📉 Histogram (Height Distribution)
plt.figure(figsize=(10, 6))
plt.hist(df["Height"], bins=10, edgecolor='black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.savefig("Graphs/height_histogram.png")
plt.show()

# Part 5: Insights
# Region with tallest hill
tallest_region = df.loc[df["Height"].idxmax(), "Region"]
# Most common category
most_common_category = df["Height Category"].value_counts().idxmax()
# Distribution summary
distribution_summary = df["Height"].describe()
print(tallest_region)
print(most_common_category)
print(distribution_summary)
print("========================================================")
