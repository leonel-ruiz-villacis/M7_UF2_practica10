import pandas as pd

"""df = pd.read_csv('lista.csv')
print(df)
"""


def density_per_m2(cities_df):
    cities_df['Density per M2'] = cities_df['Population']
    return cities_df[{'City', 'Density  M2'}]


cities_df = pd.read_csv("lista.csv")
print(density_per_m2(cities_df))





