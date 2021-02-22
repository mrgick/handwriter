from PIL import Image
import random
import os

#global dir path
path = os.path.abspath(os.curdir)+'/'

#create array from lines from file
def read_file(file_name):
	f = open(file_name,'r')
	data = f.read()
	f.close()
	data = data.split('\n')
	return data

#inser one symbol in image
def insert_symbol(img_source,symbol_name,px,py):
	if symbol_name =='.':
		symbol_name = 'point'
	if symbol_name == '/':
		symbol_name = 'div'
	path_symbols = path + 'symbols/' + symbol_name
	if os.path.exists(path_symbols) == True:
		
		#chose one symbol
		num = 1
		path2 =path_symbols+'/'+str(num)+'.png'
		while os.path.exists(path2) == True:
			num = num+1
			path2=path+'/'+str(num)+'.png'
		num = int(random.uniform(1,num))

		img_letter = Image.open(path_symbols+'/'+str(num)+'.png')

		#change size
		rresize = int(random.uniform(-3,3))
		img_letter = img_letter.resize((img_letter.size[0]+rresize, img_letter.size[1]+rresize), Image.ANTIALIAS)
		px_img_size = img_letter.size[0]		

		#rotate
		rrot = random.uniform(-3,3)
		img_letter=img_letter.rotate(rrot,Image.BILINEAR,expand=True)

		#insert in image	
		px = px+ int(random.uniform(2,6))
		rpy = int(random.uniform(0,4))
		img_source.alpha_composite(img_letter, (px, py+rpy))
		px = px+px_img_size
	
	else:
		print('there are no symbol:'+symbol_name)
	return img_source,px



#creating line with symbols
def line_create(symbols_str,paper='clear'):
	px = 0
	py = 0
	img_line = Image.open(path+'background/line_place_'+paper+'.png')
	for i in range(len(symbols_str)):

		if symbols_str[i]!=" " and symbols_str[i]!="\t":
			symbol = symbols_str[i].lower()

			#change some symbols
			if symbol=='┌' or symbol=='┬' or symbol=='┐' or symbol=='└' or symbol=='┴' or symbol=='┘' or symbol=='─':
				symbol = '-'
			elif symbol=='│' or symbol=='├' or symbol=='|' or symbol=='┼' or symbol=='┤': 
				symbol='l'

			img_line,px = insert_symbol(img_line,symbol,px,py) 
			px = px
		else:
			px = px+20+int(random.uniform(-10,10))
	return img_line


#show array with text in image
def array_to_png(arr):
	source_img = Image.open(path+'background/clear.png')
	py=159
	for j in range(len(arr)):
		px = 15+int(random.uniform(-10,10))
		img_line = line_create(arr[j],'clear')
		source_img.alpha_composite(img_line, (px, py))
		px = px

		#py = py + 59 #one square
		if j == 13:
			py = py+118+59
		else:
			py = py + 118 #two square
	return source_img


def main():

	#symbols that I draw
	symbols = "abcdefghijklmnopqrstuvwxyz0123456789:;,'<>=*().-+/_абввгдеёжзиклмопрстуфхцчшщъыьэюя"

	#s = read_file('path to file')
	s = [symbols,symbols,symbols]
	source_img = array_to_png(s)

	#word = "somethin"
	#source_img = line_create(word)
	
	source_img.show()
	source_img.save("output/output.png")

if __name__=="__main__":
	main()