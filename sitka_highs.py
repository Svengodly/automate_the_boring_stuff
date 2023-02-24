import csv

import matplotlib.pyplot as plt

from datetime import datetime


filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    # print(header_row)
    # ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
    for row in reader:
        current_date = datetime.strptime(row[header_row.index("DATE")], '%Y-%m-%d')
        try:
            high = int(row[header_row.index("TMAX")])
            low = int(row[header_row.index("TMIN")])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot the high temperatures.
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()

