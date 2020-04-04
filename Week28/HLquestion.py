import matplotlib.pyplot as plt 
import csv

# Data handling
with open("total_cases.csv") as dt:
    worldData = []
    norwayData = []
    dates = []
    values = csv.reader(dt, delimiter=",")
    
    for row in values:
        if "date" not in row: # Only adds the rows with numbers
            dates.append(row[0])
            worldData.append(int(row[1])) # Converts all values to ints

            if row[108] == "": # if the value is blank, it cannot be converted to int, so a 0 must be added manually
                norwayData.append(0)
            else:
                norwayData.append(int(row[108]))


fig, ax1 = plt.subplots()

plt.title("Comparison of COVID-19 cases in the World and Norway")

# Configure first y-axis (world data)
ax1.set_xlabel("time")
ax1.set_ylabel("World cases")
ax1.plot(dates,worldData, "b-")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx() #Instantiate a second axes that shares the same x-axis

# Configure the second y-axis (norway data)
ax2.set_ylabel("Norway cases", color="tab:red")
ax2.plot(dates, norwayData, "r-")
ax2.tick_params(axis="y", labelcolor="tab:red")


plt.xticks(dates[::2])
fig.autofmt_xdate()

plt.show()
