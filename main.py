from PIL import Image
import random
import os

#глобальный путь
path = os.path.abspath(os.curdir)+'/'

#символы, которые я нарисовал
symbols = "abcdefghijklmnopqrstuvwxyz0123456789:;,'<>=*().-+/_абввгдеёжзиклмопрстуфхцчшщъыьэюя"

#чтение файла
def read_file(file_name):
	f = open(file_name,'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	return data

#вставка буквы в изображение
def insert_letter(img_source,symbol_name,px,py):
	if symbol_name =='.':
		symbol_name = 'point'
	if symbol_name == '/':
		symbol_name = 'div'
	path_symbols = path + 'symbols/' + symbol_name
	if os.path.exists(path_symbols) == True:
		
		#определяем кол-во вариаций и выбираем одну
		num = 1
		path2 =path_symbols+'/'+str(num)+'.png'
		while os.path.exists(path2) == True:
			num = num+1
			path2=path+'/'+str(num)+'.png'
		num = int(random.uniform(1,num))

		img_letter = Image.open(path_symbols+'/'+str(num)+'.png')

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



#создание строки с буквами
def line_create(symbols_str,paper='clear'):
	px = 0
	py = 0
	img_line = Image.open(path+'background/line_place_'+paper+'.png')
	for i in range(len(symbols_str)):

		if symbols_str[i]!=" " and symbols_str[i]!="\t":
			symbol = symbols_str[i].lower()

			#производим замену некоторых символов
			if symbol=='┌' or symbol=='┬' or symbol=='┐' or symbol=='└' or symbol=='┴' or symbol=='┘' or symbol=='─':
				symbol = '-'
			elif symbol=='│' or symbol=='├' or symbol=='|' or symbol=='┼' or symbol=='┤': 
				symbol='l'

			img_line,px = insert_letter(img_line,symbol,px,py) 
			px = px
		else:
			px = px+25+int(random.uniform(-10,10))
	return img_line


#представление печатного текста в рукописном
def array_to_png(arr):
	source_img = Image.open(path+'background/A35.png')
	py=159
	for j in range(len(arr)):
		px = 10+int(random.uniform(-10,10))
		img_line = line_create(arr[j],'clear')
		source_img.alpha_composite(img_line, (px, py))
		px = px

		#py = py + 59 #one 
		if j == 13:
			py = py+118+59
		else:
			py = py + 118 #two
	return source_img


def main():

	#s = read_file('path_to_your_file')
	s = [symbols,symbols,symbols]
	source_img = array_to_png(s)

	#source_img = line_create(symbols)
	
	source_img.show()
	source_img.save("output/output.png")

if __name__=="__main__":
	main()