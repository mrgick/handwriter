from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import random
import os

path = os.path.abspath(os.curdir)+'/'

symbols = "abcdefghijklmnopqrstuvwxyz0123456789:;,'<>=*().-+/_абввгдеёжзиклмопрстуфхцчшщъыьэюя"

def read_file(file_name):
	f = open(file_name,'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	return data

def insert_letter(img_source,symbol_name,px,py,path):
	if symbol_name =='.':
		symbol_name = 'point'
	if symbol_name == '/':
		symbol_name = 'div'
	path = path + 'symbols/' + symbol_name
	if os.path.exists(path) == True:
		
		num = 1
		path2 =path+'/'+str(num)+'.png'
		while os.path.exists(path2) == True:
			num = num+1
			path2=path+'/'+str(num)+'.png'
		num = int(random.uniform(1,num))


		img_letter = Image.open(path+'/'+str(num)+'.png')


		# изменяем размер
		rresize = int(random.uniform(-3,3))
		img_letter = img_letter.resize((img_letter.size[0]+rresize, img_letter.size[1]+rresize), Image.ANTIALIAS)
		px_img_size = img_letter.size[0]		


		#поворот
		rrot = random.uniform(-3,3)
		img_letter=img_letter.rotate(rrot,Image.BILINEAR,expand=True)

		#вставляем в картину	
		px = px+ int(random.uniform(2,6))
		rpy = int(random.uniform(0,4))
		img_source.alpha_composite(img_letter, (px, py+rpy))
		px = px+px_img_size
		
	
	else:
		print('there are no symbol:'+symbol_name)
	return img_source,px


source_img = Image.open(path+'/'+'background/A35.png')
py=159
#s = [' 1 абввгдеёжзиклмопрстуфхцчшщъыьэюя',symbols]
#s = [symbols,symbols,symbols]
#s = ["abcdefghijklmnopqrstuvwxyz0123456789","abcdefghijklmnopqrstuvwxyz0123456789","abcdefghijklmnopqrstuvwxyz0123456789"]
#s = ['Введенная точка не принадлежит фигуре','Введенная точка не принадлежит фигуре','Введенная точка не принадлежит фигуре']
#s = ['99999999999988888888888212777777666666666665555533332222111111111^^^^^^a^b:=:=:=:=:=:=:=:=:=:=:=:=,/////////////',"[[[[[[[[[фывфвфв]]]]]]]",":::::::::::","..........."]
s = read_file('/home/gick/Документы/programs/pascal/labs/2/2_1.pas')
#s = read_file('/home/gick/Документы/programs/pascal/labs/8/8.pas')
for j in range(len(s)):
	px = 10+int(random.uniform(-10,10))
	for i in range(len(s[j])):
		if s[j][i]!=" " and s[j][i]!="\t":
			symbol = s[j][i].lower()
			if symbol=='┌' or symbol=='┬' or symbol=='┐' or symbol=='└' or symbol=='┴' or symbol=='┘' or symbol=='─':
				symbol = '-'
			elif symbol=='│' or symbol=='├' or symbol=='|' or symbol=='┼' or symbol=='┤': 
				symbol='l'
			source_img,px = insert_letter(source_img,symbol,px,py,path) 
			px = px
		else:
			if j == 6:
				px = px+20+int(random.uniform(-10,10))
			else:
				px = px+25+int(random.uniform(-10,10))
	#py = py + 59 #one 
	if j == 13:
		py = py+118+59
	else:
		py = py + 118 #two
#print(s)
#source_img.show()
source_img.save("output/output.png")