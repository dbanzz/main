import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


EVPD = pd.read_csv('D:/Programming Assessment2/Electric_Vehicle_Population_Data.csv')
EVPD_drop = ['VIN (1-10)', 'DOL Vehicle ID', '2020 Census Tract', 'Vehicle Location','Postal Code', 'Base MSRP', 'Legislative District', 'Electric Utility','State']
afd_EVPD=EVPD.drop(columns=EVPD_drop)
