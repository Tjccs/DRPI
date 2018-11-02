# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from imageio import imread, imwrite
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

Img = imread('Z:/DRPI/einstein01.tif')

# 1
pond = [0.2989, 0.5870, 0.1140]
IntensPond = np.uint8((pond[0]*Img[:, :, 0].astype(float) + \
                       pond[1]*Img[:, :, 1].astype(float) + \
                       pond[2]*Img[:, :, 2].astype(float)))

# 2
S1 = imread('Z:/DRPI/ferramentas01.tif')
S2 = imread('Z:/DRPI/ferramentas02.tif')
Sub1 = abs(S2[:, :, 0].astype(float) - S1[:, :, 0].astype(float))
Sub2 = (255- S2[:, :, 0].astype(float) + S1[:, :, 0].astype(float))/2

# 3
D1 = imread('Z:/DRPI/texto01.tif')
D2 = imread('Z:/DRPI/texto02.tif')
Div = (D1[:, :, 0].astype(float)/D2[:, :, 0].astype(float))

# 4
Reg = imread('Z:/DRPI/ferramentas_bin.tif')
Mult = Reg*S1[:, :, 0]

# 5
A = imread('Z:/DRPI/einstein01.tif')
B = imread('Z:/DRPI/marilyn01.tif')
k1 = 0.5
k2 = 0.5
Ble = A
dim = A.shape

for i in range(0, dim[2]):
    Ble[:, :, i] = k1*A[:, :, i].astype(float) + k2*B[:, :, i].astype(float)

#6

plt.figure
plt.imshow(Ble)