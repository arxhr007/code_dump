from flask import Flask, request
import requests
from flask_cors import CORS
import os

mode="on"

app = Flask(__name__)
CORS(app)
@app.route('/<switch>', methods=['GET']) 
def home(switch):
 print(switch)
 global mode 
 mode = switch
 return switch

@app.route('/dataoftorch', methods=['GET']) 
def dataoftorch():
 return mode
