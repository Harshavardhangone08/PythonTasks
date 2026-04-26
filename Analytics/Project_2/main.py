# ==============================================================================
#  Project Title: Railway Gauge Data Analysis 
#  Analysing the railway gauge dataset using Numpy, Pandas and matplotlib
# ==============================================================================

#==============================================================================
#                  Importing the required libraries
#==============================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
'''
==================================================================================
                Scenario 1:Data Loading & Preprocessing 
==================================================================================
You are given the ign.csv dataset containing game reviews. 
Tasks: 
1. Load the dataset using Pandas. 
2. Display: 
○ First 5 rows (head()) 
○ Last 5 rows (tail()) 
○ Shape of dataset 
3. Remove the unnecessary column: 
○ "Unnamed: 0" (index column) 
4. Check for missing values in: 
○ score, genre, platform 
5. Handle missing values: 
○ Fill numeric column score with mean
○ Fill categorical column genre with mode
6. Ensure correct data types:
○ score → float 
○ release_year, release_month, release_day → integer 
'''
#1.1
df=pd.read_csv("ign.csv")
#1.2.1
print("First 5 rows from the dataset:")
print(df.head())  #to display first 5 rows
#1.2.2
print("Last 5 rows from the dataset:")
print(df.tail())  #to display last 5 rows
#1.2.3
print(f"Shape of Dataset:{df.shape}")   #to display shape of dataset
#1.3
df=df.drop(columns="Unnamed: 0")
print(df)
#1.4
print("Null values:")
print(df[["score","genre","platform"]].isnull().sum())
#1.5
df['score']=df['score'].fillna(df['score'].mean())
df['genre']=df['genre'].fillna(df['genre'].mode()[0])
#print(print(df[["score","genre","platform"]].isnull().sum()))
#1.6
df['score']=df["score"].astype(float) #to convert score to float
release=["release_year","release_month","release_day"]
df[release]=df[release].apply(pd.to_numeric,errors='coerce') #convert to integer
print(df.dtypes)
'''
==================================================================================
           Scenario 2: Line Graph (Score Trend) + Save 
==================================================================================
You want to analyze how game scores change over time. 
Tasks: 1. Group data by release_year.
2. Calculate average score per year using Pandas. 
3. Convert results into NumPy arrays. 
4. Plot a line graph: 
○ X-axis → release_year 
○ Y-axis → average score 
5. Add: 
○ Title: "Average Game Score Over Years" 
○ Axis labels 
6. Save the graph: plt.savefig("avg_score_trend.png")
'''
#2.1
group=df.groupby('release_year')['score']
#2.2
avg_score=group.mean().reset_index()
#2.3
avg_numpy=avg_score.to_numpy()
#2.4 2.5 2.6
plt.plot(avg_numpy[:,0],avg_numpy[:,1],marker='o',color='steelblue')
plt.title("Average Game Score Over Years")
plt.xlabel("Year")
plt.ylabel("Average score")
plt.savefig("Graphs/avg_score_trend.png")
plt.show()
'''
==================================================================================
                Scenario 3: Filtering + Bar Chart + Save
==================================================================================
You want to compare top platforms. 
Tasks: 1. Filter dataset where: ○ score > 7 
2. Count number of high-rated games per platform. 
3. Select top 10 platforms using Pandas. 
4. Convert data into NumPy arrays. 
5. Plot a bar chart: 
○ X-axis → platform 
○ Y-axis → count of games 
6. Rotate x-axis labels for readability. 
Save the graph: plt.savefig("top_platforms_bar.png") 
'''
#3.1
df2=df[df["score"]>7]
#print(df2["score"])
#3.2
platforms_count=df2.groupby('platform')['score'].count().reset_index()
platforms_count.columns=['Platform','count']
#print(count)
#3.3
top=platforms_count.sort_values('count',ascending=False)
top10=top.head(10)
#3.4
Platforms=top10['Platform'].to_numpy()
Count=top10['count'].to_numpy()
#3.5
plt.figure(figsize=(10,5))
plt.bar(Platforms,Count,width=0.5)
plt.title("Top platforms")
plt.xlabel("Platform")
plt.ylabel("Count of games")
plt.xticks(rotation=70)
plt.savefig("Graphs/top_platforms_bar.png")  #3.6
plt.show()
'''
==================================================================================
                Scenario 4: Aggregation + Pie Chart + Save 
==================================================================================
You want to analyze genre distribution. 
Tasks: 
1. Count the number of games per genre. 
2. Select top 5 genres using Pandas. 
3. Prepare labels and values. 
4. Plot a pie chart: 
○ Labels → genre 
○ Values → count 
5. Add percentage labels (autopct). 
Save the graph: plt.savefig("genre_distribution.png")
'''
N_games=df['genre'].value_counts().reset_index() #4.1
N_games.columns=['genre','games']
N_games_5=N_games.head() #4.2
#print(N_games_5)
labels=N_games_5["genre"]   #4.3
values=N_games_5["games"]
plt.pie(values,explode=(0.06,0,0,0,0),labels=labels,shadow=True,autopct='%1.1f%%',startangle=90)  #4.4 4.5
plt.savefig("Graphs/genre_distribution.png")
plt.show()

'''
==================================================================================
                Scenario 5: Advanced Analysis + Multiple Graphs
================================================================================== 
You are asked to perform a detailed analysis of review patterns. 
Part 1: Feature Engineering 
1. Create a new column: 
○ score_category: 
■ score >= 9 → "Excellent" 
■ 7 <= score < 9 → "Good" 
■ < 7 → "Average" 
2. Convert editors_choice: 
○ Y → 1, N → 0 
Part 2: NumPy Analysis 
3. Use NumPy to: 
○ Calculate yearly score growth using np.diff() on average yearly scores 
Part 3: Visualizations 
Line Graph 
4. Plot trend of: 
○ Average score per release_year 
Stacked Bar Chart 
5. Show count of: 
○ score_category per release_year 
Histogram 
6. Plot distribution of: 
○ score
Part 4: Save All Graphs 
plt.savefig("score_trend.png") 
plt.savefig("score_category_stacked.png") 
plt.savefig("score_distribution.png") 
Part 5: Insights 
Identify: 
● Which years had highest scores 
● Whether high scores increased over time 
● If editors_choice correlates with high scores
'''
#Part 1: Feature Engineering 
df3=df.copy()
df3["score_category"]=np.where(df3["score"]>=9,"Excellent",np.where(df3["score"]>=7,"Good","Average"))
#print(df3.head())
df3["editors_choice"]=df3["editors_choice"].map({'Y':1,'N':0})
#print(df3["editors_choice"].head())
#Part 2: NumPy Analysis
avg_yearly=df3.groupby('release_year')['score'].mean().reset_index()
years=avg_yearly["release_year"].to_numpy()
yearly_avgScore=avg_yearly["score"].to_numpy()
score_growth=np.diff(avg_score)
growthYears=years[1:]
#plot line graph
plt.plot(years,yearly_avgScore,marker='o',linewidth=2)
plt.title("Score Trend")
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.savefig("Graphs/score_trend.png")
plt.show
#Stacked bar chart
stackedbar=df3.groupby(["release_year","score_category"]).size().unstack(fill_value=0)
stackedbar.plot(kind="bar",stacked=True,color=['black','cyan','green'])
plt.title("Score Category")
plt.xlabel("Release Year")
plt.ylabel("Count of Games")
plt.xticks(rotation=65)
plt.legend(title='Score Category')
plt.tight_layout()
plt.savefig("Graphs/score_category_stacked.png")
plt.show()
#plotting Histogram
plt.hist(df3['score'],bins=10,histtype="bar",rwidth=0.4)
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Graphs/score_distribution.png")
plt.show()
#part 5
top_years=avg_yearly.sort_values('score', ascending=False).head()
print("Top years by avg score:")
print(top_years)
positive_growth = (score_growth > 0).sum()
negative_growth = (score_growth < 0).sum()
print(f"Years with increase: {positive_growth}")
print(f"Years with decrease: {negative_growth}")
corr = df3[['score','editors_choice']].corr()
print("\nCorrelation between score and editors_choice:")
print(corr)
print(df.groupby('editors_choice')['score'].mean())