# Electric Vehicle Population Data Analysis

## Overview
This project uses Python to analyze and visualize electric vehicle registration data from the U.S. state of Washington. The analyzed dataset contains various attributes of electric vehicles, such as make, model, electric driving range, etc.

## Data set
The dataset contains the following main fields:

**VIN (1-10)**: The first 10 digits of the vehicle identification number, a unique code used to identify the vehicle.
<br>
**County**: The county in which the vehicle was registered.
<br>
**City**: The city where the vehicle is registered.
<br>
**State**: The state in which the vehicle is registered.
<br>
Postal Code: The postal code in which the vehicle is registered.
<br>
**Model Year**: The year the vehicle was produced.
<br>
**Make**: The manufacturer (brand) of the vehicle.
<br>
**Model**: The model of the vehicle.
<br>
**EV Type**: The type of electric vehicle, such as a battery electric vehicle (BEV) or a plug-in hybrid electric vehicle (PHEV).
<br>
**Clean Alternative Fuel Vehicle (CAFV) Eligibility**: Whether the vehicle qualifies as a Clean Alternative Fuel Vehicle.
<br>
**Electric range**: The vehicle’s electric range.
<br>
Base MSRP: The vehicle’s base Manufacturer’s Suggested Retail Price.
<br>
Legislative District: The legislative district in which the vehicle is registered.
<br>
DOL Vehicle ID: The vehicle's Division of Licensing (DOL) ID number.
<br>
Vehicle location: The geographical location coordinates (latitude and longitude) of the vehicle.
<br>
Electric power company: The electric power company in the power supply area.
<br>
2020 Census Tract: 2020 Census Tract Number from Vehicle Registry

## The main function
**Data preprocessing**: Determine the year data range and divide the appropriate range to facilitate subsequent visualization.
**Year data conversion**: Convert the Model Year field from numbers to string types to facilitate subsequent operations.
**Data grouping and visualization**: Group the data by year and electric vehicle type, and draw a line chart to compare changes in electric vehicle types in different years.
**Market share analysis**: Calculate the market share of the top 10 brands each year and draw a stacked column chart.
**Heatmaps**: Draw heatmaps to analyze relationships and patterns between different variables.
**Empirical cumulative distribution function (ECDF)**: Perform ECDF analysis on model years and battery ranges and draw corresponding charts.
**Violin Plot**: Use a violin plot to analyze the distributional relationship between vehicle model year and CAFV (Clean Alternative Fuel Vehicle) eligibility.
**Electric vehicle range analysis**: Analyze the electric range of battery electric vehicles (BEV) and plug-in hybrid electric vehicles (PHEV) and generate box plots.

## Instructions for use
To run this script, the following Python libraries need to be installed:
**Pandas**
**matplotlib**
**seaborn**
**numpy**
## Before running the program, make sure that the data files are located in the specified path.
