# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from imageio import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

Img = imread('C:/Users/fc48286/Downloads/lena.tif')

dim = Img.shape
tipo = Img.dtype
npix = Img.size

plt.figure
plt.imshow(Img)

#Decompor as bandas R,G,B

plt.figure(figsize=(12,3))
plt.subplot(141); plt.imshow(Img)
plt.title('Inicial'); plt.axis('off')
plt.subplot(142); plt.imshow(Img[:,:,0], 'gray')
plt.title('R'); plt.axis('off')
plt.subplot(143); plt.imshow(Img[:,:,1], 'gray')
plt.title('G'); plt.axis('off')
plt.subplot(144); plt.imshow(Img[:,:,2], 'gray')
plt.title('B'); plt.axis('off')

#Gravar Img no disco
imwrite('C:/Users/fc48286/Downloads/' + 'img1_r' + '.tif', Img[:,:, 0])
imwrite('C:/Users/fc48286/Downloads/' + 'img1_g' + '.tif', Img[:,:, 1])
imwrite('C:/Users/fc48286/Downloads/' + 'img1_b' + '.tif', Img[:,:, 2])

val = Img[25,31,0]

linha_cse = 125
coluna_cse = 118
linha_cid = 140
coluna_cid = 180
cropImg = Img[linha_cse:linha_cid,coluna_cse:coluna_cid,:]
plt.figure(); plt.imshow(cropImg);
plt.title('Crop'); plt.axis('off')

Img1 = Img*1
Img1[linha_cse:linha_cid,coluna_cse:coluna_cid,:] = 10
plt.figure(); plt.imshow(Img1)
plt.title(u'Incognita'); plt.axis('off')

#Plot de perfis


#Construir uma linha "num" pontos entre os pontos de coordenadas
#(linha, coluna): (y0, x0) e (y1, x2)
y0, x0 = 100, 50
y1, x1 = 200, 200
num = 100
y, x = np.linspace(y0, y1, num), np.linspace(x0, x1, num)

#Extrair os valores dos pixels ao longo da linha
d = np.vstack((y,x))
perfil = scipy.ndimage.map_coordinates(Img[:,:,0], 'gray')

plt.figure(figsize=(15, 3))
plt.subplot(121); plt.imshow(Img[:,:,0], 'gray')
plt.title['Inicial']; plt.axis('off')
plt.plot([x0, x1], [y0, y1], 'ro=')
plt.subplot(122); plt.plot(perfil, 'ro==')
plt.title('Perfil')