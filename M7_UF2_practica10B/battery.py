import pandas as pd

def show_battery(data):
    battery_power = data.loc[:, ["ID", "battery_power"]]
    return battery_power


data = pd.read_csv("test.csv")
battery_power = show_battery(data)
print(battery_power)