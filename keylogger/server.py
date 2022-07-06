from flask import Flask, request
import requests
from flask_cors import CORS
TOKEN = 'TOKEN'
CHAT_ID = 'CHAT ID'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET']) 
def home():
 message=request.args.get('message')
 requests.post(URL, json={'chat_id': CHAT_ID,'text': message}) 
 return {}
app.run()