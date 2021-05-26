# Coursera, Applied Data Science with Python, University of Michigan
# Course 1, Introduction to Data Science in Python
# Week 4: FINAL ASSIGNMENT

# Question: "What is the win/loss ratio's correlation
#            with the population of the city it is in?"
# PLEASE NOTE: CODE HAS BEEN MODIFIED TO ABIDE BY COURSERA HONOR CODE.
# Performs the same tasks (and a bit more) as required by the assignment
# but I have taken a different approach to perform said tasks.


import pandas as pd
import numpy as np
import scipy.stats as stats


def main():
	year = 2018
	for sport in ['MLB', 'NBA', 'NFL', 'NHL']:
		cities = get_cities(sport)
		teams = get_teams(sport, year)
		merged = get_merged(sport, cities, teams)

		r, p = stats.pearsonr(merged['population'], merged['W%'])
		print(f"League: {sport}\n\tr-value = {round(r,4)}\n\tp-value = {round(p,4)}\n")

		best = merged.iloc[0]
		worst = merged.iloc[-1]
		print(f"\t{best.name} won {round(best['W%'])}% of games (best)")
		print(f"\t{worst.name} won {round(worst['W%'])}% of games (worst)\n")


def get_cities(sport):
	cities = pd.read_html("files/big4-cities.html")[1]
	cities = cities.iloc[:-1,[0,3,5,6,7,8]]

	cities = cities.rename(columns={'Metropolitan area': 'metro', 'Population (2016 est.)[8]': 'population'})
	cities[sport] = cities[sport].str.replace(r'\[.*\]', '', regex=True)		# Remove [\w]
	cities[sport] = cities[sport].replace('—', np.nan).replace('', np.nan)
	cities = cities.dropna().reset_index()
	return cities[['metro', 'population', sport]]


def get_teams(sport, year):
	df = pd.read_csv(f"files/big4-{sport.lower()}.csv")
	df = df[df['year'] == year]
	df = df[df['team'] != df['W']]

	df['team'] = df['team'].str.replace(r'\*', '', regex=True)			# Remove *
	df['team'] = df['team'].str.replace(r'\+', '', regex=True)			# Remove +
	df['team'] = df['team'].str.replace(r'\(\d*\)', '', regex=True)		# Remove (\d)
	df['team'] = df['team'].str.replace(r' Sox', 'Sox', regex=True)		# There 2 Sox teams in MLB
	df['team'] = df['team'].str.replace(r'[\w.]* ', '', regex=True)		# REMOVE ALL BUT LAST WORD
	df['team'] = df['team'].str.strip()
	
	df = df.astype({'W': int, 'L': int})
	df['W%'] = df['W'] / (df['W'] + df['L']) * 100
	df = df.astype({'W%': float})

	df = df.reset_index()
	return df[['team', 'W%']]


def get_merged(sport, cities, teams):
	team_pattern = r'([A-Z]{0,2}[a-z0-9]*\ [A-Z]{0,2}[a-z0-9]*|[A-Z]{0,2}[a-z0-9]*)'
	merged = cities[sport].str.extract(team_pattern * 3)

	merged['metro'] = cities['metro']
	merged = pd.melt(merged, id_vars=['metro'])
	merged = merged.rename(columns={'value': 'team'})
	merged = merged.replace('', np.nan).dropna()

	merged = pd.merge(merged, cities, how='outer', on='metro')
	merged = merged.drop(columns=['variable', sport])
	merged = merged.astype({'population': int})
	
	merged['team'] = merged['team'].str.replace(' Sox', 'Sox', regex=True)    # There 2 Sox teams in MLB
	merged['team'] = merged['team'].str.replace('[\w.]* ', '', regex=True)    # REMOVE ALL BUT LAST WORD
	
	merged = pd.merge(merged, teams, how='outer', on='team')
	merged = merged.groupby('metro').agg({'W%': np.nanmean, 'population': np.nanmean})
	merged = merged.sort_values(by='W%', ascending=False)
	return merged.dropna()


if __name__ == '__main__':
	main()