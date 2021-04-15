# Foundations of Data Science: K-Means Clustering in Python
# by University of London & Goldsmiths, Coursera
# Week 4: Introducing Pandas and Using K-Means to Analyse Data


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('files/happyscore_income.csv')
df = df.rename(columns={'GDP': 'x', 'happyScore': 'y'})
df = df[['country', 'x', 'y']]
df = df.set_index('country')

# Domain Standardization of Data
df_min = np.min(df, 0)
df_max = np.max(df, 0)
df = (df - df_min) / (df_max - df_min)

# Define the datapoints of interest and drop them from the global dataframe
df_poi = df.loc[[
	'Mozambique',
	'Gabon',
	'Costa Rica'
	]]
df = df.drop(df_poi.index)

# Start of Plotting
plt.title('Foundations of Data Science: K-Means Clustering in Python\nWeek 4, Peer-graded Assignment')
plt.xlabel('GDP per Capita (normalised)')
plt.ylabel('Happiness Score (normalised)')
plt.axis([-0.1, 1.1, -0.1, 1.1])

# Plot and Label Datapoints of Interest
plt.scatter(df_poi['x'], df_poi['y'], label='Point of Interest')	#Plot the datapoints of interest
plt.plot(df_poi['x'], df_poi['y'], ls=':', alpha=0.5)				#Draw lines between the datapoints
for country in df_poi.index:
	plt.text(														#Label the datapoints on the graph
		df_poi.loc[country, 'x'] - 0.01,
		df_poi.loc[country, 'y'] + 0.01,
		f"{country}"
	)

# Plot all other Datapoints
plt.scatter(df['x'], df['y'], alpha=0.75, label='Other Countries')

plt.legend()
plt.show()