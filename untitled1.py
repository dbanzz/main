import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Retrieve data from the file and perform operations
EVPD = pd.read_csv('D:/Programming Assessment2/Electric_Vehicle_Population_Data.csv')
#Remove some data that is not relevant to the analysis
EVPD_drop = ['VIN (1-10)', 'DOL Vehicle ID', '2020 Census Tract', 'Vehicle Location','Postal Code', 'Base MSRP', 'Legislative District', 'Electric Utility','State']
afd_EVPD=EVPD.drop(columns=EVPD_drop)

#Because the amount of data is too large to facilitate analysis, a random sampling method was used to extract 1,000 pieces of data for further analysis.
sample_size = 1000
EVPD_sampled = afd_EVPD.sample(n=sample_size, random_state=1)


#Line Chart
#Convert year to string type for subsequent operations
EVPD_sampled['Model Year'] = EVPD_sampled['Model Year'].astype(str)

#Since we need to draw the types of electric vehicles that change according to the year, we need to classify the data.
EVPD_count = EVPD_sampled.groupby(['Model Year', 'Electric Vehicle Type']).size().unstack()

#Draw a line chart comparing changes in electric vehicle types according to year
plt.figure(figsize=(15, 8))
sns.lineplot(data=EVPD_count, marker='o')
plt.title('Electric Vehicle Type Trends by Model Year ')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.grid(True)
plt.legend(title='Electric Vehicle Type', loc='upper left')
plt.show()


#Bar Chart
#Group the data and then count the quantity, then install the year grouping to select the top ten manufacturers of each year, and finally reshape the data, with year as the row and manufacturer as the column.
tmpy = EVPD_sampled.groupby(['Model Year', 'Make']).size().groupby(level=0, group_keys=False).nlargest(10).unstack()

#Set appropriate graph size
fig, ax1 = plt.subplots(figsize=(15, 8))

#Draw a Bar chart(Shows the annual changes in the number of electric vehicles registered by the top 10 manufacturers)
tmpy.plot(kind='bar', stacked=True, ax=ax1, colormap='tab20', alpha=0.8)

#Set labels and titles
ax1.set_xlabel('Model Year')
ax1.set_ylabel('Number of Vehicles(Top 10)')
ax1.set_title('Top 10 Electric Vehicle Makes Market Share by Year')

#Put legends on the upper left
ax1.legend(loc='upper left')

#Show bar chart
plt.xticks(rotation=0)
plt.grid(True)
plt.show()


#Heatmap
#Calculate the top ten cities and car models, and then calculate the data that meets these two conditions at the same time, and then calculate the specific values.
tc = EVPD_sampled['City'].value_counts().head(10).index
tm = EVPD_sampled['Model'].value_counts().head(10).index
tcm = EVPD_sampled[EVPD_sampled['City'].isin(tc) & EVPD_sampled['Model'].isin(tm)]
dtcm = tcm.groupby(['City', 'Model']).size().unstack().fillna(0)

#Set figure size, draw a heat map, and display values without decimal points on the heat map
plt.figure(figsize=(15, 8))
sns.heatmap(dtcm, annot=True, fmt=".0f", cmap='viridis')
plt.title('Top 10 Vehicle Models in Top 10 Cities (Heatmap)')
plt.xlabel('Model')
plt.ylabel('City')
plt.tight_layout()
plt.show()


#Empirical Cumulative Distribution Function Chart
#Calculate the number of data points through a function, sort the data as x, and calculate the data points to generate a cumulative proportion
def ecdf(data):
    n = len(data) 
    x = np.sort(data)
    y = np.arange(1, n+1) / n 
    return x, y

#Use the defined ecdf function to calculate the model year sorted data and corresponding proportions
xmy, ymy = ecdf(EVPD_sampled['Model Year'])

#Use the defined ecdf function to calculate the electric vehicle mileage data and the corresponding ratio
xer, yer = ecdf(EVPD_sampled['Electric Range'])

#Set figure size
plt.figure(figsize=(14, 6))

#Set the first cumulative distribution chart on the left, using model year data and corresponding proportion data.
plt.subplot(1, 2, 1)
plt.plot(xmy, ymy, marker='.', linestyle='none')
plt.xlabel('Model Year')
plt.ylabel('ECDF')
plt.title('ECDF of Model Year')

#Set the first cumulative distribution chart on the Right, using electric vehicle mileage data and corresponding proportion data.
plt.subplot(1, 2, 2)
plt.plot(xer, yer, marker='.', linestyle='none', color='orange')
plt.xlabel('Electric Range')
plt.ylabel('ECDF')
plt.title('ECDF of Electric Range')
plt.tight_layout()
plt.show()