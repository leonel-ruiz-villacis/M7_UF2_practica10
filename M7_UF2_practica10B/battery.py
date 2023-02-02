import pandas as pd

def show_battery():
    battery_power = pd.read_csv('test.csv', usecols=['id', 'battery_power'])
    ba = battery_power.iloc[[3, 13, 34, 56, 70, 85, 110, 120, 210, 400]]
    return ba
