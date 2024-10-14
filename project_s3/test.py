from flask import Flask, jsonify , render_template
import serial
import threading
import time

app = Flask(__name__)

# Configuration for the serial port
SERIAL_PORT = '/dev/ttyUSB0'  # Update this if your serial port is different
BAUD_RATE = 9600
SERIAL_TIMEOUT = 1  # Timeout for serial reading in seconds

# Shared variable to store the latest line read from the serial port
latest_line = None
line_lock = threading.Lock()

# Initialize the serial connection
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=SERIAL_TIMEOUT)
    time.sleep(2)  # Wait for the serial connection to initialize
    print(f"Connected to serial port {SERIAL_PORT} at {BAUD_RATE} baud.")
except serial.SerialException as e:
    ser = None
    print(f"Failed to connect to serial port {SERIAL_PORT}: {e}")

def read_serial():
    global latest_line
    if ser is None:
        print("Serial port is not initialized. Exiting serial reading thread.")
        return

    try:
        while True:
            if ser.in_waiting:
                line = ser.readline().decode('utf-8', errors='replace').strip()
                with line_lock:
                    latest_line = line
                #print(f"Read line: {line}")
            time.sleep(0.1)  # Slight delay to prevent CPU overutilization
    except Exception as e:
        print(f"Error while reading from serial port: {e}")

# Start the serial reading thread
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

@app.route('/call', methods=['GET'])
def call():
    with line_lock:
        if latest_line:
            return jsonify({"result": int(latest_line)}), 200
        else:
            return jsonify({"error": "No data received from serial port yet."}), 503

@app.route('/')
def index():
    return render_template('index.html')

def shutdown_serial():
    if ser and ser.is_open:
        ser.close()
        print("Serial port closed.")

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Shutting down.")
    finally:
        shutdown_serial()
