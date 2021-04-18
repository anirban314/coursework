# Coursera, Applied Data Science with Python, University of Michigan
# Course 1, Introduction to Data Science in Python
# Week 4: Answering Questions with Messy Data

# A demo of the unreliability of p-values and how easy it is to generate
# datasets with statistically significant difference using random numbers


import numpy as np
import pandas as pd
from scipy.stats import ttest_ind

size = (30,100000)
df1 = pd.DataFrame(np.random.random(size=size))
df2 = pd.DataFrame(np.random.random(size=size))

alpha = 0.0001
n_diff = 0

for column in df1.columns:
	t_val, p_val = ttest_ind(df1[column], df2[column])
	t_val = round(t_val, 4)
	p_val = round(p_val, 4)

	if p_val <= alpha:
		print(f"Statistically Different: Column {column}\t  t-value = {t_val}\t   p-value = {p_val}")
		n_diff += 1

p_diff = round(n_diff / len(df1.columns) * 100, 2)
print(f"\nA total of {n_diff} columns are different, which is {p_diff}%, at alpha = {alpha}")