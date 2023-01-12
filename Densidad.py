import pandas as pd

"""df = pd.read_csv('lista.csv')
print(df)
"""
def density_per_km2(cities_df):
    cities_df['Density per KM2'] = cities_df['Population']
    return cities_df[['City', 'Density KM2']]

"""
cities_df = pd.read_csv("lista.csv")
print(density_per_km2(cities_df))"""
