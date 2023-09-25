import csv
import matplotlib.pyplot as plt
import vonage
import matplotlib as mpl
mpl.use('TkAgg')

figure, (cel_ax, fah_ax) = plt.subplots(1, 2)  # Figures initialization
time_points = list()  # stores time data
temp_points = list()  # stores temperature data
sensor_status = False  # flag for sensor status, false if not connected
switch_status = False  # flag for switch status, false if the switch off


# read file
def read_file():
    with open('TempPlots.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            time_points.append(float(row[0]))
            temp_points.append(float(row[1]))


# This function draw the graph
def plot_data():
    # Celsius figure
    #cel_ax.plot(time_points, temp_points, linewidth=2, marker='.')
    cel_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Celsius)")  # ADD xlim=(-310, 10), ylim=(-50, 100) if need limit
    cel_ax.set_title("Temperature Data in Celsius")
    cel_ax.yaxis.tick_right()

    # Fahrenheit figure
    fah_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Fahrenheit)")  # ADD xlim=(-310, 10), ylim=(-100, 200) if need limit
    fah_ax.set_title("Temperature Data in Fahrenheit")
    fah_ax.yaxis.tick_right()

    for time, temp, time_label, temp_label in zip(time_points, temp_points, time_points, temp_points):
        temp_fahr_points = temp * 9 / 5 + 32
        # plot data
        cel_ax.plot(time, temp, color='red', linewidth=2, marker='.')
        fah_ax.plot(time, temp_fahr_points, color='blue', linewidth=2, marker='.')
        # add label
        cel_ax.annotate(str(temp_label), xy=(time_label, temp_label))
        fah_ax.annotate(str(temp_fahr_points), xy=(time_label, temp_fahr_points))
        plt.pause(0.01)


    # Fahrenheit figure
    '''
    temp_fahr_points = [(i * 9 / 5 + 32) for i in temp_points]
    fah_ax.plot(time_points, temp_fahr_points, linewidth=2, marker='.')
    plt.pause(0.01)
    fah_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Fahrenheit)")  # ADD xlim=(-310, 10), ylim=(-100, 200) if need limit
    fah_ax.set_title("Temperature Data in Fahrenheit")
    fah_ax.yaxis.tick_right()
    # Add the label for temperature data
    for i, j in zip(time_points, temp_fahr_points):
        fah_ax.annotate(str(j), xy=(i, j))
    '''

def add_points():
    plt.pause(0.01)
    cel_ax.plot([20, 50, 100], [24, 25, 21], linewidth=2, marker='.')
    fah_ax.plot([20, 50, 100], [77, 88, 99], linewidth=2, marker='.')


def check_switch():
    # Display "No Data Available" if the switch is off
    if not switch_status:
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        cel_ax.text(0.05, 0.87, "No Data Available", transform=cel_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
        fah_ax.text(0.05, 0.87, "No Data Available", transform=fah_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)


def check_sensor():
    # Display "Unplugged Sensor" if the sensor is not connected
    if not sensor_status:
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        cel_ax.text(0.05, 0.95, "Unplugged Sensor", transform=cel_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
        fah_ax.text(0.05, 0.95, "Unplugged Sensor", transform=fah_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)


def show():
    plt.show()


# Send text message to a phone number
def send_sms(msg):
    client = vonage.Client(key="b97abc26", secret="ognhX5rUby9tMLxy")
    sms = vonage.Sms(client)
    if msg == 0:
        response_data = sms.send_message(
            {
                "from": "15713965612",
                "to": "13194129046",
                "text": "Temperature too low!",
            }
        )
    else:
        response_data = sms.send_message(
            {
                "from": "15713965612",
                "to": "13194129046",
                "text": "Temperature too high!",
            }
        )
    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")


def main():
    global sensor_status
    global switch_status
    read_file()
    plot_data()
    check_switch()
    check_sensor()
    add_points()
    show()


if __name__ == "__main__":
    main()
