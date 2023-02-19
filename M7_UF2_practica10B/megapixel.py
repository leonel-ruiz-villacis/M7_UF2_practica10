import pandas as pd

def show_megapixels(data):
    print(get_megapixels(data))

def get_megapixels(data):
    megapixels = data.loc[:, 'pc']
    return megapixels