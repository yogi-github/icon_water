import pandas as pd
import matplotlib.pyplot as plt

def readfile(filename):
	# Read the Excel File and create Dataframes
	xls = pd.ExcelFile(filename)
	df_yu = pd.read_excel(xls, 'year_usage')
	df_au = pd.read_excel(xls, 'area_usage')
	return (df_yu, df_au)

def plot_per_year(df_yu):
	# Chart 1
	plt.subplot(2,2,1)
	plt.title('Water Usage and Income per Year')
	plt.ylabel('Water_Usage (ML)')
	plt.plot(df_yu['year'], df_yu['water_usage_ml'], 'r-.')

	# Chart 2
	plt.subplot(2,2,3)
	plt.ylabel('Income (AUD)')
	plt.xlabel('Year')
	plt.bar(df_yu['year'], df_yu['income'])

def plot_per_area(df_au):
	# Chart 3
	plt.subplot(2,2,2)
	plt.title('Water Usage per Area')
	x_axis = range(len(df_au['area']))
	plt.xticks(x_axis, df_au['area'], rotation='vertical')
	plt.ylabel('Water_Usage (ML)')
	plt.bar(x_axis, df_au['water_usage_ml'], color='bgrcmyk')

if __name__ == '__main__':
	filename = r'input_data.xlsx'
	df_yu, df_au = readfile(filename)

	plot_per_year(df_yu)
	plot_per_area(df_au)
	plt.show()