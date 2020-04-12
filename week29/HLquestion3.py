import matplotlib.pyplot as plt 
import csv

# Covid data handling
with open("total_cases.csv") as dt:
    worldData = []
    dates = []
    values = csv.reader(dt, delimiter=",")
    
    for row in values:
        if "date" not in row: # Only adds the rows with numbers (excludes titles)
            dates.append(row[0])
            worldData.append(int(row[1])) # Converts all values to ints

# Gold data handling
with open("goldPrices.csv") as dt:
    goldPrices = []
    goldDates = []
    values = csv.reader(dt, delimiter=",")

    for row in values:
        data = list(row)[0].split(";")
        if "Time" in data:
            continue

        goldDates.append(data[0])

        avgPrice = (float(data[2]) + float(data[3])) / 2
        goldPrices.append(avgPrice)

goldDates.reverse()

# Transform the date data from gold dataset to same formwat as corona dataset (YYYY-MM-DD)
for i, date in enumerate(goldDates):
    timeMeasurements = date.split("/")
    year = timeMeasurements[2]
    month = timeMeasurements[0]
    day = timeMeasurements[1]
    goldDates[i] = f"{year}-{month}-{day}"

# Fill in missing data. 
# Simulate dates with blank data by adding the previous data to that day
for i, covidDate in enumerate(dates):
    goldDate = goldDates[i]

    if goldDate != covidDate: # If the dates do not match for the same index:
        goldDates.insert(i, covidDate) # The correct date is added
        goldPrices.insert(i, goldPrices[i-1]) # Goldprices are updated by adding the previous value to that index


# Creating the plots
fig, (ax1, ax2) = plt.subplots(2) # Using .subplot() to create two separate plots

ax1.plot(dates, worldData, "b")
ax1.set_ylabel("Global covid-19 cases")

ax2.plot(dates, goldPrices, "r")
ax2.set_ylabel("Gold prices (USD)")

# Format x-axis as dates, with interval of 2 (for space issues)
plt.xticks(dates[::2])
fig.autofmt_xdate()

plt.show()

