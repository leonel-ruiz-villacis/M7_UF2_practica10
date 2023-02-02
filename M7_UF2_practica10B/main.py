import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import battery as ba
import megapixel as me
import Microprocesacodor as mi


print(ba.show_battery())
print("--------------")
print(me.show_megapixels())
print("--------------")
print(mi.show_processor_speed())
print("--------------")


def main(data):
    processor_speed = mi.show_processor_speed()
    megapixels = me.show_megapixels()
    battery_power = ba.show_battery()

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    processor_speed.bar(kind='bar', x='id', y='clock_speed', ax=ax1, legend=False)
    ax1.set_title("clock_speed")
    megapixels.bar(kind='bar', x='id', y='px_width', ax=ax2, legend=False)
    ax2.set_title("px_width")
    battery_power.bar(kind='bar', x='id', y='Battery_power', ax=ax3, legend=False)
    ax3.set_title("Battery_power")

    plt.legend()
    plt.show()

main()

'''def show_processor_speed(data):
    processor_speed = data.loc[:, ["ID", "Processor Speed"]]
    return processor_speed


def show_megapixels(data):
    megapixels = data.loc[:, ["ID", "Megapixels"]]
    return megapixels


def show_battery_power(data):
    battery_power = data[['ID', 'Battery_power']]
    return battery_power.iloc[[3, 13, 34, 56, 70, 85, 110, 120, 210, 400]]


def main(data):
    processor_speed = show_processor_speed(data)
    megapixels = show_megapixels(data)
    battery_power = show_battery_power(data)

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15,5))
    processor_speed.plot(kind='bar', x='ID', y='Processor_speed', ax=ax1, legend=False)
    ax1.set_title("Processor Speed")
    megapixels.plot(kind='bar', x='ID', y='Megapixels', ax=ax2, legend=False)
    ax2.set_title("Megapixels")
    battery_power.plot(kind='bar', x='ID', y='Battery_power', ax=ax3, legend=False)
    ax3.set_title("Battery_power")

    plt.legend()
    plt.show()

    data = pd.read_csv("test.csv")
    main(data)'''

#if __name__ == "__main__":
 #   main()

