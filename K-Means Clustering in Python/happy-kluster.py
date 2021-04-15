# Foundations of Data Science: K-Means Clustering in Python
# by University of London & Goldsmiths, Coursera
# Week 4: Introducing Pandas and Using K-Means to Analyse Data


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from sklearn.cluster import KMeans


df = pd.read_csv('files/happyscore_income.csv')
df = df.rename(columns={'GDP': 'x', 'happyScore': 'y'})
df = df[['country', 'x', 'y']]
df = df.set_index('country')


# Domain Standardization of Data
df_min = np.min(df, 0)
df_max = np.max(df, 0)
df = (df - df_min) / (df_max - df_min)


# Calculating GLOBAL Mean and Standard Deviation
df_mean = np.mean(df, 0)
df_stdv = np.std(df, 0)


# Computing K-Means Clustering
no_of_clusters = 3
clustered = KMeans(n_clusters=no_of_clusters).fit(df[['x', 'y']])
k_means = np.sort(clustered.cluster_centers_, 0)
k_label = clustered.labels_


# Start of Plotting
fig, graph = plt.subplots()
plt.title('Happiness and World Bank Income inequality Gini measure (2015)')
plt.xlabel('GDP per Capita  (normalised)')
plt.ylabel('Happiness Score  (normalised)')
plt.axis([-0.1, 1.1, -0.1, 1.1])


# Plotting CLUSTER Means (connecting lines)
graph.plot(k_means[:,0], k_means[:,1], c='red', ls='--', alpha=0.1)


# Plotting the CLUSTER Datapoints
df['c'] = k_label
for i in range(no_of_clusters):
	dfc = df.where(df['c'] == i).dropna()
	graph.scatter(dfc['x'], dfc['y'], alpha=0.9, label=f"Cluster {i+1}")	


# Plotting CLUSTER Means (points)
graph.scatter(k_means[:,0], k_means[:,1], c='black', s=25, label='Cluster means')


# Plotting GLOBAL Mean
graph.scatter(df_mean['x'], df_mean['y'], c='red', s=100, alpha=0.75, label='Global mean')


# Plotting GLOBAL Standard Deviation Ranges
for i in range(1, 6):
	graph.add_patch(
		patch.Ellipse(
			[df_mean['x'], df_mean['y']],	# x and y coordinates
			df_stdv['x'] * i,				# stdv of x, i.e. width
			df_stdv['y'] * i,				# stdv of y, i.e. height
			ec='r',
			fill=False,
			alpha=0.1
		)
	)
	graph.text(
		df_mean['x'] - df_stdv['x'] / 2 * i,
		df_mean['y'],
		f" {i}.SD",
		color='r',
		alpha=0.2
	)


plt.legend()
plt.show()