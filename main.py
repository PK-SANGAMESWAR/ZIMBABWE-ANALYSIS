import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

##Load the datasets
life_df=pd.read_csv("./data/LifeExpectency.csv")
gdp_df=pd.read_csv("./data/GDPperCapita.csv")

#Rename the columns
life_df.columns=['Year','Life Expectency']
gdp_df.columns=['Year','GDP Per Capita']

##convert 'year' to int->year
life_df['Year']=life_df['Year'].astype(int)
gdp_df['Year']=gdp_df['Year'].astype(int)

##Merge 2 datasets on Year
merged_df=pd.merge(life_df,gdp_df,on='Year',how='inner')

##plot the data
print(merged_df.head())

##Line plot of Life Expectency
plt.plot(life_df['Year'],life_df['Life Expectency'],color='green')
plt.title('Life Expectency over time')
plt.xlabel('Year')
plt.ylabel('Life Expectency')
plt.grid(True)
plt.show()


##Line plot of GDP Per Capita
plt.plot(gdp_df['Year'],gdp_df['GDP Per Capita'],color='blue')
plt.title('GDP Per Capita over time')
plt.xlabel('Year')
plt.ylabel('GDP Per Capita (USD)')
plt.grid(True)
plt.show()


##Scatter Plot of GDP Per Captita
sns.set(style='whitegrid')
plt.figure(figsize=(10,6))
sns.scatterplot(data=merged_df,
x='GDP Per Capita',
y='Life Expectency',
color='crimson',
s=80)
plt.xscale('log')
plt.title('GDP Per Capita vs Life Expectency (Zimbabwe)', fontsize=14)
plt.xlabel('GDP Per Capita (log scale)', fontsize=12)
plt.ylabel('Life Expectency (Years)', fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')

plt.figure(figsize=(12, 7))
scatter = sns.scatterplot(
    data=merged_df,
    x='GDP Per Capita',
    y='Life Expectency',
    color='crimson',
    s=80
)

plt.xscale('log')
plt.title('GDP Per Capita vs Life Expectancy (Zimbabwe)', fontsize=14)
plt.xlabel('GDP Per Capita (log scale)', fontsize=12)
plt.ylabel('Life Expectency (Years)', fontsize=12)
plt.grid(True, which="both", ls="--", linewidth=0.5)

# 👉 Annotate each point with the year
for i in range(len(merged_df)):
    year = merged_df.iloc[i]['Year']
    x = merged_df.iloc[i]['GDP Per Capita']
    y = merged_df.iloc[i]['Life Expectency']
    
    # Special formatting for crisis years (e.g., 1995–2005)
    if 1995 <= year <= 2005:
        plt.text(x, y, str(year), fontsize=9, color='blue')
    else:
        plt.text(x, y, str(year), fontsize=8, alpha=0.6)

plt.tight_layout()
plt.show()
plt.tight_layout()
plt.show()

##Histogram of merged_df
plt.hist(merged_df['Life Expectency'], bins=10)


#  Create a new column for Decade
merged_df['Decade'] = (merged_df['Year'] // 10) * 10

# Set theme
sns.set(style='whitegrid')

#  Boxplot for Life Expectancy by Decade
plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Decade',
    y='Life Expectency',
    data=merged_df,
    palette='Greens'
)
plt.title('Life Expectancy by Decade (Zimbabwe)', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Life Expectancy (Years)', fontsize=12)
plt.tight_layout()
plt.show()


#  Boxplot for GDP per Capita by Decade
plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Decade',
    y='GDP Per Capita',
    data=merged_df,
    palette='Blues'
)
plt.title('GDP Per Capita by Decade (Zimbabwe)', fontsize=14)
plt.xlabel('Decade', fontsize=12)
plt.ylabel('GDP Per Capita (USD)', fontsize=12)
plt.tight_layout()
plt.show()
