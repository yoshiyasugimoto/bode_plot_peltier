# import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# csv_path = "./peltier_data/OP_12_13.csv"
csv_path = "./peltier_data/OP2_12_13.csv"

df = pd.read_csv(csv_path, names=("Frequency[Hz]", "Gain[dB]", "Phase[degree]"))

fig = plt.figure()
ax1 = fig.add_subplot()
ax2 = ax1.twinx()

x_axe = plt.gca().set_xscale("log")

ax1.plot(df["Frequency[Hz]"], df["Gain[dB]"], label="Gain[dB]")
ax1.grid(which="minor")
ax1.set_ylabel("Gain[dB]")
ax1.yaxis.set_major_locator(ticker.MultipleLocator(10)) #axes1:interval
ax1.set_xlabel("Frequency[Hz]")

ax2.plot(df["Frequency[Hz]"], df["Phase[degree]"], label="Phase[degree]", color="r")
ax2.yaxis.set_major_locator(ticker.MultipleLocator(45))  #axes2:interval
ax2.set_ylabel("Phase[degree]")

plt.show()
