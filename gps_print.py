import serial
import pynmea2

port = "/dev/ttyAMA0"
ser = serial.Serial(port, baudrate=9600, timeout=0.5)

try:
    while True:
        newdata = ser.readline()
        n_data = newdata.decode('latin-1')
        if n_data.startswith('$GNGGA'):
            newmsg = pynmea2.parse(n_data)
            lat = newmsg.latitude
            lng = newmsg.longitude
            gps = f"Latitude={lat} and Longitude={lng}"
            print(gps)
except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()