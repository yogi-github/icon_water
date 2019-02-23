# Data visualization task

The data visualization is done by using Tableau and Python Script with input data as an Excel file.

## Sample Charts
Sample charts created using Tableau is in folder **Charts_using_tableau**

Sample charts created using Python Script is in file **charts_using_matplotlib**


## Python Script
A python script that takes Excel file as an input and visualizes the data in charts.

**Libraries used** - Matplotlib, Pandas, Xlrd

**Input data** - input_data.xlsx


### Follow the steps below to run the script (as per windows environment)

1. Assume **Python 3.x** and **Pip** is installed

2. Install and Activate Virtual environment
	- python -m pip install -U virtualenv
	- virtualenv ENV
	- cd ENV/Scripts
	- activate

3. Install the required libraries
	- pip install -r requirements.txt

4. Run the python script
	- python draw_chart.py

5. A chart pop up
	- Please maximize and view the charts


## Enhancements
- It is possible to read data from Databases and visualize directly 