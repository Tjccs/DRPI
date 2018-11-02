# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 09:28:02 2018

@author: fc48286
"""

from imageio import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import scipy.misc
import scipy.stats


Img = imread('Z:/DRPI/imagens/marilyn.tif')
dim = Img.shape
col = dim[1]
lin = dim[0]

miu = 0
var = 0.1
U = np.random.uniform(-1, 1, [lin, col])
G = np.sqrt(var)*255*U+miu
Rg =(Img.astype(float)+G.astype(float)).clip(0, 255)


densidade = 2.0/100
sp = np.random.random_sample([lin, col])
px_escuros = sp<(densidade/2)
px_claros = (sp>=(densidade/2)) & (sp<densidade)
rsp = Img.astype(float)+(~px_escuros).astype(float)
rsp = 255*(px_claros.astype(float))+rsp*(~px_claros).astype(float)

gauss_denoised = ndimage.filters.gaussian_filter(Img, 1)

median_denoised = ndimage.filters.gaussian_filter(Img, 3)

plt.figure(figsize=(10, 5))
plt.title('###### Questão 1.1 c) ######')
plt.imshow(gauss_denoised)
plt.axis('off')

m = 3
mat = np.ones((m,m))