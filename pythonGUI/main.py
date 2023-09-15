import csv
import matplotlib.pyplot as plt
import vonage

time_points = list()    # stores time data
temp_points = list()    # stores temperature data
sensor_status = False   # flag for sensor status, false if not connected
switch_status = False   # flag for switch status, false if the switch off


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

    # Display "No Data Available" if the switch is off
    if not switch_status:
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        cel_ax.text(0.05, 0.87, "No Data Available", transform=cel_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
        fah_ax.text(0.05, 0.87, "No Data Available", transform=fah_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)

    # Display "Unplugged Sensor" if the sensor is not connected
    if not sensor_status:
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        cel_ax.text(0.05, 0.95, "Unplugged Sensor", transform=cel_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)
        fah_ax.text(0.05, 0.95, "Unplugged Sensor", transform=fah_ax.transAxes, fontsize=10,
                    verticalalignment='top', bbox=props)

    plt.show()


# Send text message to a phone number
def send_sms():
    client = vonage.Client(key="b97abc26", secret="ognhX5rUby9tMLxy")
    sms = vonage.Sms(client)

    response_data = sms.send_message(
        {
            "from": "15713965612",
            "to": "13194129046",
            "text": "Hello World!",
        }
    )

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")


def main():
    read_file()
    plot()


if __name__ == "__main__":
    main()
