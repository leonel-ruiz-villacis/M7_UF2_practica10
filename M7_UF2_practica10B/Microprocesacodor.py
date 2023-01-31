import pandas as pd

def show_processor_speed(data):
    processor_speed = data.loc[:, ["ID", "Processor Speed"]]
    return processor_speed

# Exemple d'ús:
data = pd.read_csv("test.csv")
processor_speed = show_processor_speed(data)
print(processor_speed)
