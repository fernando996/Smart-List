import requests
import os
import pyimgur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def cameraConfig() :
	try:
		file = open("Camera.Conf", "r") 
		#lines = text_file.read().split(',')
		aux = file.read().split('\n')
		aux.pop()
		return aux 
	
	except KeyboardInterrupt:
		return 
	except:
		return "Error Reading Camera Config!!!"


def takePicture( array , foto ):
	try:
		for i in array:
			auxFoto = foto + 1
			img_data = requests.get("http://"+i+"/photo.jpg").content
			with open('imagem_'+str(auxFoto)+'.jpg', 'wb') as handler:
				handler.write(img_data)
			return auxFoto
	except KeyboardInterrupt:
		#return
		print("Keyboard")
		return 0
	except:
		print ("Take Picture Error!")
		return 0

def uploadImage (CLIENT_ID, fotoAnterior, fotoAtual): 
	linkList = []
	im = pyimgur.Imgur(CLIENT_ID)
	try:
		auxFoto = fotoAnterior
		while fotoAtual > auxFoto : 
			auxFoto = auxFoto + 1
			path = str(os.getcwd()) + "/imagem_"+ str(auxFoto) + ".jpg"
			uploaded_image = im.upload_image(path, title="imagem_"+ str(auxFoto))
			linkList.append(str(uploaded_image.link))
		return linkList
	except KeyboardInterrupt:
		print("Keyboard")
		return 
	except:
		print ("Upload Error!")
		return 

def search(linkList):
	searchList = []
	try:
		driver = webdriver.Firefox()

		for i in linkList:
			driver.get("https://www.google.com/searchbyimage?&image_url="+ i)

			#assert "Python" in driver.title
			elem = driver.find_element_by_class_name("fKDtNb")
			print (elem.text)
			searchList.append(elem.text)
		driver.close()
		return searchList
	except KeyboardInterrupt:
		print("Keyboard")
		return 
	except:
		print ("Search Error")
		return 
	


