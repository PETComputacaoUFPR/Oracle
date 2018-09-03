
from PIL import Image, ImageDraw
import os, sys

QR_SIZE = 350

A4_X = 2480
A4_Y = 3508

BLOCK_X = 6
BLOCK_Y = 9
N_BLOCK = BLOCK_X * BLOCK_Y

PAD_X = int((A4_X - (BLOCK_X*QR_SIZE)) / BLOCK_X)
PAD_Y = int((A4_Y - (BLOCK_Y*QR_SIZE)) / BLOCK_Y)
print(PAD_X,PAD_Y)

path = "./img/"

def saveBlock(output, files):
    blank_image = Image.new("1",(A4_X,A4_Y), color=1)
    #~ blank_image.paste(foreground, (0, 0), foreground)
   


    for i,f in enumerate(files):
        
        f = Image.open(f)
        
        count_x = int(i%BLOCK_X)
        count_y = int(i/BLOCK_X)
        x = count_x * QR_SIZE  +  count_x * PAD_X
        y = count_y * QR_SIZE  +  count_y * PAD_Y
        
        #~ new_size = (354, 354)
        #~ new_im = Image.new("1", new_size, color=0)
        #~ x+=20
        #~ y+=20
        #~ blank_image.paste(new_im, (x-2,y-2))
        
        blank_image.paste(f, (x,y))
        
        
        
    blank_image.save(output)

i = 0
stop = False
while(not stop):
    files=[]
    for j in range(N_BLOCK):
        nameFile = path+str(i+j)+".png"
        if(os.path.isfile(nameFile)):
            files.append(nameFile)
        else:
            stop = True
    
    saveBlock("img/output/"+str(int(i/N_BLOCK))+".png",files)
    i+=N_BLOCK
