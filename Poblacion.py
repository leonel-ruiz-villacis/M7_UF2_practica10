import pandas as pd

"""df = pd.read_csv('lista.csv')"""
#print(df)


def total_population(cities_df):
    return cities_df[['City', 'Population']].groupby(['City']).sum()


"""cities_df = pd.read_csv("lista.csv")
print(total_population(cities_df))"""

