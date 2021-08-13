# Foundations of Data Science: K-Means Clustering in Python
# by University of London & Goldsmiths, Coursera
# Week 5: A Data Clustering Project


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patch
from sklearn.cluster import KMeans

# V1. Variance of Wavelet Transformed image (continuous)			1. Real - 762
# V2. Skewness of Wavelet Transformed image (continuous)			2. Fake	- 610

df = pd.read_csv('files/banknote-authentication.csv')

# Computing K-Means Clustering
no_of_clusters = 2
clustered = KMeans(n_clusters=no_of_clusters).fit(df)
k_means = clustered.cluster_centers_
k_label = clustered.labels_

df['c'] = k_label
df_k0 = df.where(df['c'] == 0).dropna()
df_k1 = df.where(df['c'] == 1).dropna()
print(df)

# Exploratory Data Analysis
df_mean = np.mean(df, 0)
df_stdv = np.std(df, 0)

df_k0_mean = np.mean(df_k0, 0)
df_k0_stdv = np.std(df_k0, 0)

df_k1_mean = np.mean(df_k1, 0)
df_k1_stdv = np.std(df_k1, 0)


# Start of Plotting
fig, graph = plt.subplots()
plt.title('Friend of the Bank')
plt.xlabel('V1. Variance')
plt.ylabel('V2. Skewness')

# Plotting the Datapoints
for i in range(no_of_clusters):
	plot_sd = 2
	dfc = df.where(df['c'] == i).dropna()
	dfc_mean = np.mean(dfc, 0)
	dfc_stdv = np.std(dfc, 0)

	graph.scatter(dfc['V1'], dfc['V2'], alpha=0.4, label=f"Cluster {i+1}")
	graph.add_patch(
		patch.Ellipse(
			[dfc_mean['V1'], dfc_mean['V2']],		# x and y coordinates
			dfc_stdv['V1'] * plot_sd,				# stdv of x, i.e. width
			dfc_stdv['V2'] * plot_sd,				# stdv of y, i.e. height
			ec='r',
			ls=':',
			fill=False,
			alpha=1
		)
	)


# Plotting CLUSTER Means
graph.scatter(k_means[:,0], k_means[:,1], c='black', s=25, alpha=0.75, label='Cluster means')


# Plotting GLOBAL Mean
graph.scatter(df_mean['V1'], df_mean['V2'], c='red', s=50, alpha=1, label='Global mean')


plt.legend()
plt.show()