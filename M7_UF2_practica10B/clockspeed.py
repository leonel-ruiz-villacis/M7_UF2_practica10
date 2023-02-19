import pandas as pd

def show_clock_speed(data):
    print(get_clock_speed(data))

def get_clock_speed(data):
    clock_speed = data.loc[:, 'clock_speed']
    return clock_speed
