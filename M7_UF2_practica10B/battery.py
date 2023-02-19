import pandas as pd

def show_battery(data):
    print(get_battery(data))

def get_battery(data):
    battery_power = data.loc[:, 'battery_power']
    return battery_power