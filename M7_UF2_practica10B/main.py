import pandas as pd
import matplotlib.pyplot as plt


def show_processor_speed(data):
    processor_speed = data.loc[:, ["ID", "Processor Speed"]]
    return processor_speed


def show_megapixels(data):
    megapixels = data.loc[:, ["ID", "Megapixels"]]
    return megapixels


def show_battery_power(data):
    battery_power = data[['ID', 'Battery_power']]
    return battery_power


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
    main(data)

#if __name__ == "__main__":
 #   main()

