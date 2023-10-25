import csv
import matplotlib.pyplot as plt
import vonage
import matplotlib as mpl
import socket

mpl.use('TkAgg')

figure, (cel_ax, fah_ax) = plt.subplots(1, 2)  # Figures initialization
time_points = list()  # stores time data
temp_points = list()  # stores temperature data
sensor_status = False  # flag for sensor status, false if not connected
switch_status = False  # flag for switch status, false if the switch off
props = dict(boxstyle='round', facecolor='red', alpha=0.5)
switch_text_cel = cel_ax.text(0.05, 0.87, "No Data Available", transform=cel_ax.transAxes, fontsize=10,
                              verticalalignment='top', bbox=props, visible=True)
switch_text_fah = fah_ax.text(0.05, 0.87, "No Data Available", transform=fah_ax.transAxes, fontsize=10,
                              verticalalignment='top', bbox=props, visible=True)
sensor_text_cel = cel_ax.text(0.05, 0.95, "Unplugged Sensor", transform=cel_ax.transAxes, fontsize=10,
                              verticalalignment='top', bbox=props, visible=True)
sensor_text_fah = fah_ax.text(0.05, 0.95, "Unplugged Sensor", transform=fah_ax.transAxes, fontsize=10,
                              verticalalignment='top', bbox=props, visible=True)


# read file
def read_file():
    with open('TempPlots.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            time_points.append(float(row[0]))
            temp_points.append(float(row[1]))


# This function draw the graph initially
def plot_data():
    # Celsius figure
    # cel_ax.plot(time_points, temp_points, linewidth=2, marker='.')
    cel_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Celsius)")  # ADD xlim=(-310, 10), ylim=(-50, 100) if need limit
    cel_ax.set_title("Temperature Data in Celsius")
    cel_ax.yaxis.tick_right()

    # Fahrenheit figure
    fah_ax.set(xlabel="Time (seconds ago)",
               ylabel="Temperature (Fahrenheit)")  # ADD xlim=(-310, 10), ylim=(-100, 200) if need limit
    fah_ax.set_title("Temperature Data in Fahrenheit")
    fah_ax.yaxis.tick_right()


# Take in two parameters time and temp, then add them onto graph
def add_points(time, temp):
    cel_ax.plot(time, temp, color='blue', linewidth=2, marker='.')
    fah_ax.plot(time, temp * 9 / 5 + 32, color='blue', linewidth=2, marker='.')
    # add label
    cel_ax.annotate(str(temp), xy=(time, temp))
    fah_ax.annotate(str(temp * 9 / 5 + 32), xy=(time, temp * 9 / 5 + 32))


def check_switch():
    # Display "No Data Available" if the switch is off
    if not switch_status:
        plt.setp(switch_text_cel, visible=True)
        plt.setp(switch_text_fah, visible=True)
    else:   # set the text invisible when the switch is on
        plt.setp(switch_text_cel, visible=False)
        plt.setp(switch_text_fah, visible=False)


def check_sensor():
    # Display "Unplugged Sensor" if the sensor is not connected
    if not sensor_status:
        plt.setp(sensor_text_cel, visible=True)
        plt.setp(sensor_text_fah, visible=True)
    else:   # set the text invisible when the sensor is connected
        plt.setp(sensor_text_cel, visible=False)
        plt.setp(sensor_text_fah, visible=False)


# Send text message to a phone number
def send_sms(msg):
    client = vonage.Client()
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


# Act as server, show interactive graph
def server_program():
    global sensor_status
    global switch_status
    plot_data()
    check_switch()
    check_sensor()
    plt.pause(0.001)

    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data_array = data.split(',')

        # Send sms if the temperature is too low or too high
        if "null" not in data_array[1]:
            if float(data_array[1]) < 0:
                send_sms(0)
        elif "null" not in data_array[1]:
            if float(data_array[1]) > 50:
                send_sms(1)

        # Set the sensor and switch status
        if int(data_array[2]) == 0:
            sensor_status = False
        else:
            sensor_status = True
        if float(data_array[3]) == 0:
            switch_status = False
        else:
            switch_status = True

        # Add points to the graph
        if "null" not in data_array[0] and "null" not in data_array[1]:
            add_points(float(data_array[0]), float(data_array[1]))
            plt.pause(0.01)
        # check switch and sensor status, and then display text on graph
        check_switch()
        check_sensor()
        plt.pause(0.01)
        plt.pause(0.01)  # make sure it doesn't delay
        # conn.send(data.encode())  # send data to the client

    plt.show()
    conn.close()  # close the connection


def main():
    global sensor_status
    global switch_status
    read_file()
    plot_data()
    check_switch()
    check_sensor()
    add_points(25, 30)
    plt.show()


if __name__ == "__main__":
    server_program()
