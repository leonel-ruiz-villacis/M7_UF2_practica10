import pandas as pd

def show_processor_speed():
    processor_speed = pd.read_csv('test.csv', usecols=['id', 'clock_speed'])
    mi = processor_speed.iloc[[2, 12, 33, 46, 50, 75, 210, 320, 350, 400]]
    return mi
