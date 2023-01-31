import pandas as pd

def show_megapixels(data):
    megapixels = data.loc[:, ["ID", "Megapixels"]]
    return megapixels


data = pd.read_csv("test.csv")
megapixels = show_megapixels(data)
print(megapixels)
