import csv
import matplotlib.pyplot as plt
import numpy as np

### read file
def read_file():
    with open('TempPlots.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)


# This function draw the graph
def plot():
    read_file()
    time_points = np.array([-300, -200, -100, -50, 0, 10])
    temp_points = np.array([24, 23, 21, 20.5, 25, 20])

    f = plt.figure()
    ax = f.add_subplot(111)
    ax.yaxis.tick_right()

    # Set bounds
    plt.xlim([-310, 10])
    plt.ylim([-50, 80])

    # Plot
    plt.plot(time_points, temp_points, linewidth=2, marker='.')
    plt.title("Temperature Data")
    plt.xlabel("Time (seconds ago)")
    plt.ylabel("Temperature (Celsius)")

    plt.show()


plot()
