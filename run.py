from GPS.GPS import gpsRead
if __name__ == '__main__':
    data = gpsRead("/dev/ttyACM0",9600) # Change the port and baudrate accordingly Example: (Windows: COM1, Linux: /dev/ttyACM0)
    while True:
        GPS_Coordinates = data.get_position()
        print(GPS_Coordinates)