import matplotlib.pyplot as plt
import numpy as np

# This function draw the graph
def plot():
    timePoints = np.array([-300, -200, -100, -50, 0, 10])
    tempPoints = np.array([24, 23, 21, 20.5, 25, 20])

    f = plt.figure()
    ax = f.add_subplot(111)
    ax.yaxis.tick_right()

    # Set bounds
    plt.xlim([-310, 10])
    plt.ylim([-50, 80])

    # Plot
    plt.plot(timePoints, tempPoints)
    plt.title("Temperature Data")
    plt.xlabel("Time (seconds ago)")
    plt.ylabel("Temperature (Celsius)")

    plt.show()

plot()
