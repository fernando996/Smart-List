import Functions as fs

CLIENT_ID = "24753a15c46d761"
fotoAnterior = 0
fotoAtual = 0
confCamera = fs.cameraConfig()

while 1 : 

	fotoAtual = fs.takePicture(confCamera, fotoAtual)
	
	linkList = fs.uploadImage (CLIENT_ID, fotoAnterior, fotoAtual)

	fotoAnterior = fotoAnterior + len(linkList)

	fs.search(linkList)


