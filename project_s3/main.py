import serial
import requests
import time

serial_port = '/dev/ttyUSB0'
baud_rate = 9600


ser = serial.Serial(serial_port, baud_rate)
time.sleep(2)

try:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            print(line)


except KeyboardInterrupt:
    print("Exiting...")
finally:
    ser.close()
