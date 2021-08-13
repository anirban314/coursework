import itertools
import numpy as np
import matplotlib.pyplot as plt

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
size = 10000
dist = np.array([
    
    np.random.triangular(-2, 0, 2, size),
    np.random.normal(0, 2, size),
    np.random.gamma(3, 1, size),
    np.random.exponential(1, size)
])
titles = ['Triangular', 'Normal', 'Gamma', 'Exponential']
colors = ['tab:green', 'tab:blue', 'tab:orange', 'tab:red']

fig, axs = plt.subplots(2, 4, figsize=(10,5))
axs = list(itertools.chain(*axs))

for i in range(len(axs)):
    if i<4:
        axs[i].hist(dist[i], density=True, bins=100, alpha=0.8, color=colors[i])
    else:
        axs[i].scatter(dist[i-4], range(len(dist[i-4])), s=1, alpha=0.3, color=colors[i-4])
        axs[i].set_title(titles[i-4], size='small', color='darkslateblue', weight='semibold')
    
    axs[i].axis('off')
    

fig.suptitle('An Animated Demonstration of various Distribution Patterns', size='medium', color='darkslateblue', weight='semibold')
plt.subplots_adjust(left=0.03, right=0.97, bottom=0.04, top=0.92, wspace=0.05, hspace=0.15)
plt.show()