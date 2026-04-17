import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson
df=pd.read_csv("Netflix_Title.csv")
'''print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Not Available")
df["country"] = df["country"].fillna("N/A")
df.dropna(subset=["date_added"], inplace=True)
df.drop_duplicates(inplace=True)
df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')
df.dropna(subset=["date_added"], inplace=True)
df["year_added"] = df["date_added"].dt.year
print(df.isnull().sum())
print(df.head())
print(df["type"].unique())
#Pie chart
type_counts = df["type"].value_counts()
plt.figure()
df["type"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.show()
#Line Chart
year_counts=df["year_added"].value_counts().sort_index()
plt.figure()
plt.plot(year_counts.index, year_counts.values,marker='D',mec="Gray",mfc="Gold")
plt.title("Netflix Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("No.of Shows")
plt.show()
#Top Countries (Bar Chart)
country_counts=df["country"].value_counts().head(15)
plt.figure()
country_counts.plot(kind="bar")
plt.title("Top 15 Countries with Most Netflix Content")
plt.xlabel("Countries")
plt.ylabel("No.of Shows")
plt.xticks(rotation=45)
plt.show()
#Ratings Analysis (TV-MA, PG etc.)
rating_counts=df["rating"].value_counts()
plt.figure()
sns.barplot(x=rating_counts.index,y=rating_counts.values)
plt.title("Netflix Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("No.of Shows")
plt.xticks(rotation=45)
plt.show()
#Duration Analysis "poisson"
movies=df[df["type"]=="Movie"].copy()
movies["duration"]=movies["duration"].str.replace("min","")
movies["duration"]=pd.to_numeric(movies["duration"],errors="coerce")
new_df=movies["duration"].dropna()
new_df.plot(kind="hist",density=True,bins=30)
lam=new_df.mean()
a=np.arange(min(new_df),max(new_df))
plt.plot(a, poisson.pmf(a, lam), color='purple')        
plt.title("Netflix Movie Duration Distribution")
plt.xlabel("Movie Duration (Minutes)")
plt.ylabel("Frequency")
plt.show()'''
#Missing Values Heatmap
df=pd.read_csv("Netflix_Title.csv")
top = df["country"].value_counts().head(10).index
new_df=df[df["country"].isin(top)].groupby(["country","type"]).size().unstack()
new_df = new_df.fillna(0)
sns.heatmap(new_df,annot=True,cmap='coolwarm',linewidths=0.5,center=0)
plt.title("Netflix Content: Country vs Type Heatmap")
plt.show()

'''df = pd.read_csv("Netflix_Title.csv")
# Top 10 countries only
top = df["country"].value_counts().head(10).index
new_df = df[df["country"].isin(top)].groupby(["country","type"]).size().unstack()
new_df = new_df.fillna(0)
sns.heatmap(new_df, annot=True)
plt.title("Country vs Type")
plt.show()'''
