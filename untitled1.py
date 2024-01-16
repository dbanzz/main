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
