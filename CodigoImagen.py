import numpy as np
import cv2
from matplotlib import pyplot as plt

#Leer imagen
img=cv2.imread('paisaje-otonal.jpg',0)
img1=cv2.imread('paisaje-otonal.jpg',0)
img2=cv2.imread('paisaje-otonal.jpg',0)
img3=cv2.imread('paisaje-otonal.jpg',0)
img4=cv2.imread('paisaje-otonal.jpg',0)
img5=cv2.imread('paisaje-otonal.jpg',0)
img6=cv2.imread('paisaje-otonal.jpg',0)
img7=cv2.imread('paisaje-otonal.jpg',0)
img8=cv2.imread('paisaje-otonal.jpg',0)
imgn=cv2.imread('mustang.jpg',0)
bgr_img = cv2.imread('paisaje-otonal.jpg')

b,g,r = cv2.split(bgr_img)       
rgb_img = cv2.merge([r,g,b])    

#cv2.imshow('Original', img)
#Umbral 
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        if(img1[i,j]>=170):
            img1[i,j]=255
        else:
            img1[i,j]=0
            
#Umbral Binario,Invertido
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if(img2[i,j]<=65 or img2[i,j]>=220):
            img2[i,j]=255
        else:
            img2[i,j]=0

#Umbral escalas de grises
for i in range(img3.shape[0]):
    for j in range(img3.shape[1]):
        if(img3[i,j]<=65 or img3[i,j]>=220):
            img3[i,j]=255

#Operador de extension
for i in range(img4.shape[0]):
    for j in range(img4.shape[1]):
        if(img4[i,j]<=65 or img4[i,j]>=220):
            img4[i,j]=0
        else:
            img4[i,j]=(img4[i,j]-65)*((255/220)-65)
            
#Operador reduccion del nivel de gris                      
for i in range(img5.shape[0]):
    for j in range(img5.shape[1]):
        if(img5[i,j]<=51):
            img5[i,j]=0
        elif(img5[i,j]>51 and img5[i,j]<102):
            img5[i,j]=51
        elif(102<img5[i,j] and img5[i,j]<153):
            img5[i,j]=102
        elif(153<img5[i,j] and img5[i,j]<204):
            img5[i,j]=153
        elif(204<img5[i,j] and img5[i,j]<255):
            img5[i,j]=204

#Adicion de dos imagenes
img6=(img+imgn)/2

#sustraccion de dos imagenes
img7=2*(img-imgn)

#operaciones logicas: negacion, or, and y xor.                      
for i in range(img8.shape[0]):
    for j in range(img8.shape[1]):
        if(img8[i,j]<=51):
            img8[i,j]=0
        elif(img8[i,j]>51 and img8[i,j]<102):
            img8[i,j]=1
        elif(102<img8[i,j] or img8[i,j]<153):
            img8[i,j]=0
        elif(153<img8[i,j] ^ img8[i,j]<204):
            img8[i,j]=1
        elif not(204<img8[i,j] and img8[i,j]>255):
            img8[i,j]=0

titulos = ['Imagen Original' ,'Inverso Negativo','Umbral', 'Umbral Binario' , ' Umbral Binario Invertido' ,
           'Umbral Grises','Umbral Grises Invertido','Operador Extension','Reduccion Gris',
           'Adicion','Sustraccion','Operaciones Logicas']
imagenes = [rgb_img, 255-img, img1, img2, 255-img2, img3,255-img3, img4,img5,img6,
            img7,img8]
for i in xrange(12):
    plt.subplot(3,4,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(titulos[i])
    plt.xticks([]),plt.yticks([])
plt.show()

