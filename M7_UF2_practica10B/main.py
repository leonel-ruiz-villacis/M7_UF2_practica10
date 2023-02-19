import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import battery as ba
import megapixel as me
import clockspeed as cs


def main():
    file = pd.read_csv('test.csv', usecols=['id', 'clock_speed', 'battery_power', 'pc'], index_col=0)
    data = file.loc[[3, 13, 34, 56, 70, 85, 110, 120, 210, 400]]

    clock_speed = cs.get_clock_speed(data)
    megapixels = me.get_megapixels(data)
    battery_power = ba.get_battery(data)

    plt.close("all")

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    ax1.set_title('Clock speed')
    clock_speed.plot.bar(ax=ax1, rot=0, legend=True)

    ax2.set_title('Camera megapixels')
    megapixels.plot.bar(ax=ax2, rot=0, legend=True)

    ax3.set_title('Battery power')
    battery_power.plot.bar(ax=ax3, rot=0, legend=True)

    plt.show()

if __name__ == "__main__":
   main()

