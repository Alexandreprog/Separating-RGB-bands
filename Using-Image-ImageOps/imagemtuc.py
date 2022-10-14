from PIL import Image, ImageOps

img_original = Image.open("/content/Captura de tela 2022-10-08 184230.png")

width, height = img_original.size#pega a largura e a altura da imagem

img_original = img_original.resize((width, height))#função para redimensionar a imagem, não foi necessária nesse caso

img_RBGAbands = Image.Image.split(img_original)#Separa as imagens nas bandas RGBA, mas deixa sem as cores, apenas separa

display(img_original)

img_Rband = img_RBGAbands[0]# Separando cada 
img_Gband = img_RBGAbands[1]# banda em uma
img_Bband = img_RBGAbands[2]# imagem diferente

img_Rband = ImageOps.colorize(img_Rband,black="black", white="red")#Colorindo cada
img_Gband = ImageOps.colorize(img_Gband,black="black", white="green")# banda com sua
img_Bband = ImageOps.colorize(img_Bband,black="black", white="blue")# respectiva cor associada 

display(img_Rband)
display(img_Gband)
display(img_Bband)
