import csv
import matplotlib.pyplot as plt

time_points = list()  # stores time data
temp_points = list()  # stores temperature data


# read file
def read_file():
    with open('TempPlots.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            time_points.append(float(row[0]))
            temp_points.append(float(row[1]))


# This function draw the graph
def plot():
    # time_points = [-300, -200, -100, -50, 0, 10]
    # temp_points = [24, 23, 21, 20.5, 25, 20]

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


def main():
    read_file()
    plot()
