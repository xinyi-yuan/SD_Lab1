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

    figure, (cel_ax, fah_ax) = plt.subplots(1, 2)

    # Celsius figure
    cel_ax.plot(time_points, temp_points, linewidth=2, marker='.')
    cel_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Celsius)")  # ADD xlim=(-310, 10), ylim=(-50, 100) if need limit
    cel_ax.set_title("Temperature Data in Celsius")
    cel_ax.yaxis.tick_right()

    # Fahrenheit figure
    temp_fahr_points = [(i * 9 / 5 + 32) for i in temp_points]
    fah_ax.plot(time_points, temp_fahr_points, linewidth=2, marker='.')
    fah_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Fahrenheit)")  # ADD xlim=(-310, 10), ylim=(-100, 200) if need limit
    fah_ax.set_title("Temperature Data in Fahrenheit")
    fah_ax.yaxis.tick_right()

    plt.show()


def main():
    read_file()
    plot()


if __name__ == "__main__":
    main()
