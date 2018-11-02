# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:23:54 2018

@author: fc48286
"""

from imageio import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
import scipy.misc

Img = imread('Z:/DRPI/imagens/meia_cara.tif')
dim = Img.shape
col = dim[1]
lin = dim[0]


saturacao = 0
c = 0
d = 255
elc, elc1 = np.zeros((lin, col, dim[2]))
helc, helc1 = np.zeros((256, 3))
ha = np.zeros((256, 3))

for i in range(dim[2]):
    a = float(np.min(Img[:, :, i]))
    b = float(np.max(Img[:, :, i]))
    elc[:, :, 1] = (Img[:, :, i].astype(float)-a)*((d-c)/(b-a))+c
    ha[:, i] = np.cumsum(h[:, i])
    bot = ha[:, i]/(lin*col)
    a1 = float(np.count_nonzero(bot<=saturacao/2)-1)
    b1 = float(np.count_nonzero(bot<=(1-saturacao/2)-1))
    elc1[:, :, i] = ((Img[:, :, i].astype(float)-a1) * \
                    ((d-c)/(b1-a1))+c).clip(min=0, max=255)