#! /usr/bin/python3
"""
This code is specificaly designed for my computer so that the screen size,font size ,font positon etc... should be changed into your needdddddddd;)

and the way this works is kinda shit ,

and,
if it works ,it works thats all;) 

"""



from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import system
from pynput.keyboard import Listener
from pathlib import Path
home=Path.home()
word = ""
cou=0
en=0
system(f"gsettings set org.gnome.desktop.background picture-uri file:////usr/share/word-wallpaper/black.jpg")
def change(x):
	img = Image.open('/usr/share/word-wallpaper/black.jpg')
	I1 = ImageDraw.Draw(img)
	myFont = ImageFont.truetype('FreeMono.ttf', 100)
	I1.text((250, 800), x, font=myFont, fill =(255, 0, 0))
	img.save(f"{home}/bg.png")
	system(f"gsettings set org.gnome.desktop.background picture-uri file:///{home}/bg.png")
def on_press(key):
	global word,cou,en
	if len(str(key)) == 3:
		cou+=1
		en+=1
		word+=str(key)[1:-1]
		change(word)
	elif str(key) == "Key.space":
		cou+=1
		en+=1
		word+=" "
		change(word)
	elif str(key) == "Key.backspace":
		cou-=1
		en-=1
		word=word[:-1]
		change(word)
	if str(key) == "Key.enter" or cou == 41:
		word+="\n"
		en+=41-cou
		cou=0
		change(word)
	if en == 534:
		en=0
		cou=0
		word=""
		system(f"gsettings set org.gnome.desktop.background picture-uri file:////usr/share/word-wallpaper/black.jpg")

with Listener(on_press=on_press) as listener:
	listener.join()
