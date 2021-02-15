from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random

symbols = "abcdefghijklmnopqrstuvwxyz0123456789:;,'<>=*().-+/"

def read_file(file_name):
	f = open(file_name,'r')
	data = f.read()
	f.close()
	return data.split('\n')

def insert_letter(img_source,letter_name,px,py):
	if letter_name =='.':
		letter_name = 'point'
	if letter_name == '/':
		letter_name = 'div'
	img_letter = Image.open('symbols/'+letter_name+'/1.png')
	rrot = random.uniform(-3,3)
	rpx = int(random.uniform(0,2))
	rpy = int(random.uniform(0,4))
	img_source.alpha_composite(img_letter.rotate(rrot), (px+rpx, py+rpy))
	return img_source,px+img_letter.size[0]


source_img = Image.open('background/paper.png')
py=0
s = [' 1',symbols]
#s = read_file('your file')

for j in range(len(s)):
	px = 10+int(random.uniform(-5,5))
	for i in range(len(s[j])):
		if s[j][i]!=" " and s[j][i]!="\t":
			source_img,px = insert_letter(source_img,s[j][i].lower(),px,py) 
			px = px
		else:
			px = px+30+int(random.uniform(-10,10))
	#py = py + 59 #one 
	py = py + 118 #two
#print(s)
source_img.show()
#source_img.save("output/output.png")