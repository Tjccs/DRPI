# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from imageio import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import scipy.misc

"""
v4 = np.array([[92, 44], [82, 152]])
x = np.array([[0,1], [0, 1]])
y = np.array([[0, 0], [1,1]])

dy = 0.6
dx = 0.4

#vizinho mais prox.
dist = np.sqrt((dx-x)**2+(dy-y)**2)
ind = np.argwhere(dist == np.min(dist))
z_viz = v4[ind[0, 0], ind[0, 1]]
print ('Reamostragem por vizinho mais proximo', z_viz)

#interpolação bilenear
k1 = dx*v4[0, 1]+(1-dx)*v4[0, 0]
k2 = dx*v4[1, 1]+(1-dx)*v4[1, 0]
z_bil = dy*k2+(1-dy)*k1
print ('Reamostragem por interpolação bilinear', z_bil)

#interpolação bicubica
xx = np.arange(4)
v16 = np.array([[79, 46, 120, 60], [88, 92, 44, 134],
                [91, 84, 152, 77], [31, 45, 130, 178]])
a = np.arange(4)*0
plt.figure(figsize=(10, 2))
plt.subplot(121)
plt.title(u'Polinomios em x')

from scipy.interpolate import interp1d
for i in range(4):
    f = interp1d(xx, v16[i, :], kind = 'cubic')
    fcubic1 = f(np.arange(0, 3, 0.01))
    a[i] =fcubic1[int((1+dx)/0.01)]
    plt.plot(np.arange(0, 3, 0.01), fcubic1, 'g')
    plt.plot(xx, v16[i,:], 'o')

f = interp1d(xx, a, kind='cubic')
fcubic2 = f(np.arange(0, 3, 0.01))
z_bic = fcubic2[int((1+dy)/0.01)]
plt.subplot(122)
plt.plot(np.arange(0, 3, 0.01), fcubic2, 'g')
plt.plot(xx, a, 'o')
plt.title(u'Polinomio em y')
print ('Reamostragem por interpolação bicubica: ', int(z_bic))
"""
A = imread('Z:/DRPI/einstein01.tif')
dim = A.shape
import math
col1 = dim[1]
lin1 = dim[0]

xx = np.linspace(0, col1-1, col1)
yy = np.linspace(0, lin1-1, col1)
x1, y1 = np.meshgrid(xx, yy)
#Angulo
ang = 20
alfarad = np.radians(ang)
#dimensoes da nova janela
col2 = int(math.ceil(abs(col1*np.cos(alfarad)+abs(lin1*np.sin(alfarad)))))
lin2 = int(math.ceil(abs(lin1*np.cos(alfarad)+abs(col1*np.sin(alfarad)))))

#novas cordenadas dos pixeis apos rotações
x2 = x1*np.cos(alfarad)+y1*np.sin(alfarad)
y2 = -x1*np.sin(alfarad)+y1*np.cos(alfarad)
#translação para o primeiro quadrante
x2t = x2-np.min(x2)
y2t = y2-np.min(y2)
# sem translação para o primeiro quadrante 
#x2t = x2
#y2t = y2
#imagem rodada
Rd = np.zeros((int(lin2), int(col2), dim[2]))
for k1 in range(0, dim[2]):
    for k2 in range(0, lin1):
        for k3 in range(0, col1):
            Rd[int(np.round(y2t[k2,k3])), int(np.round(x2t[k2, k3])), k1] = A[k2, k3, k1]

plt.figure(figsize=(10, 5))
plt.imshow(np.uint8(Rd))
plt.title(u'Rotação processo direto. Angulo = '+ str(alfarad*180/np.pi)+' graus')
plt.axis('off')