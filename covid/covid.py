import requests as rq 
import os,time
data=rq.get("https://www.worldometers.info/coronavirus").text.splitlines()
k=data[data.index("<h1>Coronavirus Cases:</h1>")+2][25:-7]
print(k)
while True:
    data=rq.get("https://www.worldometers.info/coronavirus").text.splitlines()
    num=data[data.index("<h1>Coronavirus Cases:</h1>")+2][25:-7]
    if int(num.replace(",","").strip()) > int(k.replace(",","").strip()):
        print("increasd:",num)
        os.system("termux-torch on")
        time.sleep(3)
        os.system("termux-torch off")
        k=num

