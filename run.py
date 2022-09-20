from GPS import gpsRead
if __name__ == '__main__':
    x = gpsRead("/dev/ttyACM0",9600)
    while True:
        p = x.get_position()
        print(p)

