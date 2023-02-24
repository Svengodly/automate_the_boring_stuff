import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = "data/louisatmp.csv"

with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)
    # 0
    # STATION
    # 1
    # NAME
    # 2
    # DATE
    # 3
    # PRCP
    # 4
    # SNOW
    dates, precip, snow = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            precipitation = float(row[3])
            # snowfall = int(row[4])
        except ValueError:
            print(f"Missing value for {date}")
        else:
            dates.append(date)
            precip.append(precipitation)
            # snow.append(snowfall)

    plt.style.use('bmh')
    fig, ax = plt.subplots()
    plt.plot(dates, precip, c='blue')
    ax.set_title("Precip values for June 2022 - Louisa", fontsize=20)
    ax.set_xlabel("", fontsize=15)
    ax.set_ylabel("Amount of Precipitation", fontsize=15)
    fig.autofmt_xdate()
    # ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
