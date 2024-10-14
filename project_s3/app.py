from flask import Flask, request
import os
import logging
import serial
import requests
import time

app = Flask(__name__)

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.WARNING)
serial_port = '/dev/ttyUSB1'
baud_rate = 9600


@app.route('/call', methods=['GET'])
def call():
    result = 
    return result

if __name__ == '__main__':
    app.run()