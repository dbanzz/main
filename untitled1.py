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