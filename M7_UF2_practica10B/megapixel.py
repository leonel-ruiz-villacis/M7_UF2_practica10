import pandas as pd

def show_megapixels():
    megapixels = pd.read_csv('test.csv', usecols=['id', 'px_width'])
    me = megapixels.iloc[[1, 33, 54, 76, 80, 95, 210, 320, 330, 400]]
    return me
