from PIL import Image, ImageShow, ImageFilter, ImageDraw, ImageFont
import pandas as pd
import numpy as np

#paste function
def PasteImage(source, target, pos):
    smap = source.load()
    tmap = target.load()
    for i in range(pos[0], pos[0] + source.size[0]): # Width
        for j in range(pos[1], pos[1] + source.size[1]): # Height
            sx = i - pos[0]
            sy = j - pos[1]
            tmap[i, j] = smap[sx, sy]
    return target

#size adjustment with changes
def AdjustSize(size, start):
    result= round(start+(size*0.05))
    return result

im= Image.open('Requirements/BG.PNG')
imt= Image.open('Requirements/BGU.PNG')
imb= Image.open('Requirements/BGD.PNG')
imm= Image.open('Requirements/BGM.PNG')
logo= Image.open('Requirements/Logo.PNG')
footer= Image.open('Requirements/Footer.PNG')
headtxt= Image.open('Requirements/Headtxt.PNG')
datebg= Image.open('Requirements/Dateblue.PNG')
phonebg= Image.open('Requirements/Phonegray.PNG')
totalbg= Image.open('Requirements/Totalblue.PNG')
rial= Image.open('Requirements/Rial.PNG')
x, y= im.size

data= pd.read_csv("Price.csv")
s= data.iloc[1][5]
if s=="Samsung":
    phonelogo= Image.open('Requirements/Samsung logo.PNG')
    header= Image.open('Requirements/Header2.PNG')
    l=200
    logoloc= (390,10)
if s=="Huawei":
    phonelogo= Image.open('Requirements/Huawei logo.PNG')
    header= Image.open('Requirements/Header1.PNG')
    l=0
    logoloc= (480,10)
if s=="Xiaomi":
    phonelogo= Image.open('Requirements/Mi logo.PNG')
    header= Image.open('Requirements/Header2.PNG')
    l=200
    logoloc= (480,10)
row, col= data.shape

#change only y to add more items
size= (row-4)*67
if size<0:
    size=0
im2= im.resize((x,y+size))
im3= PasteImage(imt, im2, (0,0))
x1, y1= imt.size
x2, y2= imm.size
imm2= imm.resize((x2,y2+size))
im3= PasteImage(imm2, im3, (0,y1))
im3= PasteImage(imb, im3, (0,y1+y2-2+size))

s= data.iloc
y= round(y/7.7)
z= round(size*-0.05)+50
loc= AdjustSize(size, 55)
header= header.resize((934,40))
a, b= totalbg.size
totalbg= totalbg.resize((a-l, b))

im3= PasteImage(logo, im2, (897,47))
ysize= AdjustSize(size, 230)
im3= PasteImage(header, im3, (80,230))
ysize= AdjustSize(size, 55)
im3= PasteImage(footer, im3, (75,y1+y2-2+size))
im3= PasteImage(headtxt, im3, (300,130))
ysize= AdjustSize(size, 55)
im3= PasteImage(datebg, im3, (80,75))
for i in range(row-1):
    loc= 280+(65*i)
    im3= PasteImage(phonebg, im3, (80,loc))
    draw = ImageDraw.Draw(im3)
    for j in range(col):
        s= str(data.iloc[i][j])
        if j==0:
            font = ImageFont.truetype("Requirements/arial.ttf", 25, encoding="unic")
            draw.text(((l/3)+90+220*j, loc+20),s,(66,75,142),font=font)
        elif j==1:
            font = ImageFont.truetype("Requirements/Yekan.ttf", 26, encoding="unic")
            draw.text((l/2.1, loc+20),str(i+1),(66,75,142),font=font)
            draw.text((l+90+220*j, loc+20),s,(66,75,142),font=font)
        elif j==2:
            font = ImageFont.truetype("Requirements/Yekan.ttf", 26, encoding="unic")
            draw.text(((l/8)+90+265*j, loc+20),s,(66,75,142),font=font)
        elif j==3:
            font = ImageFont.truetype("Requirements/Yekan.ttf", 26, encoding="unic")
            draw.text((90+258*j, loc+20),s,(66,75,142),font=font)
    font = ImageFont.truetype("Requirements/arial.ttf", 17, encoding="unic")
    color= str(data.iloc[i][8])
    if color=='nan':
        color= str(data.iloc[i][7])
        if color=='nan':
            color= str(data.iloc[i][6])
            if color!='nan':
                draw.text((90+350, loc+20),color,(66,75,142),font=font)
        else:
            color= str(data.iloc[i][6])
            draw.text((90+350, loc+10),color,(66,75,142),font=font)
            color= str(data.iloc[i][7])
            draw.text((90+350, loc+30),color,(66,75,142),font=font)
        color= str(data.iloc[i][6])
    elif color!='nan':
        color= data.iloc[i][6]
        draw.text((90+350, loc+1),color,(66,75,142),font=font)
        color= str(data.iloc[i][7])
        draw.text((90+350, loc+20),color,(66,75,142),font=font)
        color= str(data.iloc[i][8])
        draw.text((90+350, loc+40),color,(66,75,142),font=font)

im3= PasteImage(totalbg, im3, (300+l,loc+65))
im3= PasteImage(phonelogo, im3, logoloc)

s= data.iloc[0][4]
draw = ImageDraw.Draw(im3)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("Requirements/Yekan.ttf", 24, encoding="unic")
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((100, 80),s,(255,255,255),font=font)
s= str(data.iloc[row-1][1])
draw.text((l+310,loc+75),s,(255,255,255),font=font)
s= str(data.iloc[row-1][3])
draw.text((835,loc+75),s,(255,255,255),font=font)
im3= PasteImage(rial, im3, (710,loc+65))

ImageShow.show(im3, title='Test')

im3.save('Sabad.PNG')