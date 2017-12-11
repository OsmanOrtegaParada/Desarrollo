import numpy as np
import cv2
from matplotlib import pyplot as plt

# Cargamos la imagen
img=cv2.imread('modenas.jpg',0)
bgr_img = cv2.imread('modenas.jpg')

b,g,r = cv2.split(bgr_img)       
rgb_img = cv2.merge([r,g,b])    


# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(img, (11,11), 0)
 
#cv2.imshow('suavizado', gauss)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 255)
 
#cv2.imshow('canny', canny)

# Buscamos los contornos
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contornos,-1,(0,0,255), 2)

titulos = ['Objetos encontrados = {}'.format(len(contornos)),'Gaussiano','Canny']
imagenes = [rgb_img,gauss,canny]
for i in xrange(3):
    plt.subplot(2,2,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(titulos[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#Se agrega metodo para el bordado de la imagen


# Cargamos la imagen
img=cv2.imread('modenas2.jpg',0)
bgr_img = cv2.imread('modenas2.jpg')
b,g,r = cv2.split(bgr_img)      
rgb_img = cv2.merge([r,g,b])
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(img, (1,1), 0)

# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, 50, 220)
 

# Buscamos los contornos
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(img,contornos,-1,(0,0,255), 2)

titulos = ['Imagen Original','Simbolos Monedas']
imagenes = [rgb_img,canny]
for i in xrange(2):
    plt.subplot(1,2,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(titulos[i])
    plt.xticks([]),plt.yticks([])
plt.show()


#Se agrega metodo para observar el contorno de las imagenes


bgr_img = cv2.imread('manzanas.jpg')
b,g,r = cv2.split(bgr_img)       
rgb_img = cv2.merge([r,g,b])     

gray = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gray, (7, 7), 0)
canny = cv2.Canny(gauss, 50, 255)

t, dst = cv2.threshold(canny, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

(_, contours, _) = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 100 and area < 10000:
        cv2.drawContours(rgb_img,contours,-1,(255,0,0), 2)

titulos = ['Contorno']
imagenes = [rgb_img]
for i in xrange(1):
    plt.subplot(1,1,i+1),plt.imshow(imagenes[i],'gray')
    plt.title(titulos[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""
cv2.imshow('contornos', src)
cv2.imshow('umbral', gray)
cv2.waitKey(0)"""








