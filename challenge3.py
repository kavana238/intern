import pandas as pd 
data = { 
"Customer_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010], 
"Gender": 
["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female"], 
"Age": [25,32,28,45,36,23,40,29,31,27], 
"City_Tier": [1,2,1,3,2,1,3,2,1,2], 
"Avg_Session_Time": [15,10,18,8,12,20,7,16,14,19],  # in minutes 
"Pages_Visited": [5,3,6,2,4,8,2,5,6,7], 
"Products_Viewed": [3,2,4,1,2,5,1,3,4,4], 
"Previous_Purchases": [2,1,3,0,1,4,0,2,3,3], 
"Discount_Used": [1,0,1,0,1,1,0,1,1,1],  # 1=Yes, 0=No 
"Total_Spend": [1200,600,1800,300,900,2500,250,1500,2000,1700] 
} 
df = pd.DataFrame(data)


# task1 - Univariate Analysis 
#total_spend
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew


plt.figure()
sns.histplot(df["Total_Spend"], kde=True)
plt.xlabel("Total Spend")
plt.ylabel("Frequency")
plt.title("Distribution of Total Spend")
print("Skewness of Total Spend:", df["Total_Spend"].skew())
plt.show()

#Avg_Session_Time
plt.figure()
df["City_Tier"].value_counts().plot(kind="bar")
plt.xlabel("City Tier")
plt.ylabel("Count")
plt.title("City Tier Distribution")
plt.show()

#City_Tier Distribution
plt.figure()
df["City_Tier"].value_counts().plot(kind="bar")
plt.xlabel("City Tier")
plt.ylabel("Count")
plt.title("City Tier Distribution")
plt.show()

#Is spending normally distributed or skewed?
#ans:Spending is positively skewed (right-skewed)

#Are there outliers in session time? 
#ans:No major outliers detected in session time.

#Which city tier dominates?
#ans:Tier 1 and Tier 2 dominate equally.


#task2 - Bivariate Analysis 
#scatterplot
#Avg_Session_Time vs Total_Spend

plt.figure()
plt.scatter(df["Avg_Session_Time"], df["Total_Spend"])
plt.xlabel("Avg Session Time")
plt.ylabel("Total Spend")
plt.title("Session Time vs Total Spend")
plt.show()

#Pages_Visited vs Total_Spend
plt.figure()
plt.scatter(df["Pages_Visited"], df["Total_Spend"])
plt.xlabel("Pages Visited")
plt.ylabel("Total Spend")
plt.title("Pages Visited vs Total Spend")
plt.show()

#Previous_Purchases vs Total_Spend
plt.figure()
plt.scatter(df["Previous_Purchases"], df["Total_Spend"])        
plt.xlabel("Previous Purchases")
plt.ylabel("Total Spend")
plt.title("Previous Purchases vs Total Spend")
plt.show()

#Boxplot
#Discount_Used vs Total_Spend 

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x="Discount_Used", y="Total_Spend", data=df)
plt.title("Discount Used vs Total Spend")
plt.xlabel("Discount Used (0=No, 1=Yes)")
plt.ylabel("Total Spend")
plt.show()


#Does discount usage increase spending? 
#ans: Yes, discount usage increases spending.


#task3 - Multivariate Analysis
#Correlation Heatmap

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Which variable most influences Total_Spend?
#ans:Previous_Purchases most strongly influences Total_Spend
#    Followed by Avg_Session_Time and Pages_Visited

# Does engagement drive revenue? 
# Yes. Engagement strongly drives revenue.
#Customers who spend more time and view more pages/products tend to spend more.


#task4 - subplot dashboard

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,8))

#  Scatter: Session vs Spend
plt.subplot(2,2,1)
plt.scatter(df["Avg_Session_Time"], df["Total_Spend"])
plt.xlabel("Avg Session Time")
plt.ylabel("Total Spend")
plt.title("Session Time vs Spend")

#  Scatter: Purchases vs Spend
plt.subplot(2,2,2)
plt.scatter(df["Previous_Purchases"], df["Total_Spend"])
plt.xlabel("Previous Purchases")
plt.ylabel("Total Spend")
plt.title("Purchases vs Spend")

#  Boxplot: Discount vs Spend
plt.subplot(2,2,3)
sns.boxplot(x="Discount_Used", y="Total_Spend", data=df)
plt.title("Discount vs Spend")
plt.xlabel("Discount Used")
plt.ylabel("Total Spend")

# Histogram: Total Spend
plt.subplot(2,2,4)
plt.hist(df["Total_Spend"], bins=5)
plt.xlabel("Total Spend")
plt.ylabel("Frequency")
plt.title("Total Spend Distribution")

plt.tight_layout()
plt.show()



#“To increase revenue by 20%, I would focus on increasing customer lifetime value by strengthening loyalty programs, 
# improving AI-based product recommendations to boost engagement, and implementing targeted discount strategies instead of mass discounting. 
# Data shows repeat purchases and engagement metrics have the strongest positive correlation with revenue, 
# so improving these drivers will sustainably increase revenue.”
