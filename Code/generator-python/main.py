#~ import pyqrcode

#~ number = pyqrcode.create("Áversaá ão %")
#~ print(number)
#~ number.show()

import numpy as np
import pyqrcode
import pandas as pd
from pyshorteners import Shortener
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import textwrap



import functools
import unidecode



def comp_func(A,B):
	A = unidecode.unidecode(A)
	B = unidecode.unidecode(B)
	if(A < B):
		return -1
	if(A > B):
		return 1
	
	return 0



# Encontra os nomes das pessoas e guarda em LongURL
LongURL = []
for l in open("nomes.txt","r"):
	LongURL.append(l.split(",")[1].replace("\n",""))

LongURL = sorted(LongURL, key=functools.cmp_to_key(comp_func))



# Cria um arquivo que poderá ser utilizado em uma página padrão para a consulta dos QRCODES
# As imagens serão salvas no diretório img/
with open('names.json', 'w') as outfile:
    outfile.write("{\"names\":"+str(LongURL)+"}")



for i in range(0,len(LongURL)):
	nameImage = LongURL[i]
	code=pyqrcode.create(nameImage)
	code.png("img/"+str(i) + '.png', scale=8, module_color=[0,0,0,128],quiet_zone=3) 
##


from PIL import Image
import os, sys

path = "./img/"
dirs = os.listdir( path )

def resize():
	for item in dirs:
		if(item.split(".")[-1] != "png"):
			continue
		if os.path.isfile(path+item):
			im = Image.open(path+item)
			f, e = os.path.splitext(path+item)
			imResize = im.resize((350,350), Image.ANTIALIAS)
			imResize.save(path+item, 'png', quality=90)

resize()


#Adds caption
MAX_W, MAX_H = 350, 350

for i in range(0,len(LongURL)):
	nameImage = LongURL[i]
	img=Image.open("img/"+str(i) + '.png')
	font = ImageFont.truetype("arial.ttf", 15)

	draw=ImageDraw.Draw(img)

	para = textwrap.wrap(nameImage, width=MAX_W)
	current_h, pad = 0, 0
	for line in para:
		w, h = draw.textsize(line, font=font)
		draw.text(((MAX_W)/2 -w/2, current_h+5), line, font=font)
		current_h += h + pad

	img.save("img/"+str(i) + '.png')
