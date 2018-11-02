# -*- coding: utf-8 -*-

from scipy import ndimage
import imageio
import matplotlib.pyplot as plt
import numpy


# Utilização do modulo imageio para ler as imagens
mars1 = imageio.imread('Z:\DRPI\questoes_aula\Mars_Reconnaissance_11.tif')
mars2 = imageio.imread('Z:\DRPI\questoes_aula\Mars_Reconnaissance_22.tif')


def sub_img(img1, img2):
    """
    :param img1: A primeira imagem .tif para a subtração
    :param img2: A segunda imagem .tif para a subtração
    :return: sub, parametro do tipo float(resultados da subtração mais realce)
    """
    sub = abs(img2.astype(float) - img1.astype(float)) > 87 # Operação Aritmetica e realce

    return sub

# Codigo disponibilizado no enunciado
D = sub_img(mars1, mars2)
ee = ndimage.generate_binary_structure(2,2)
L,n = ndimage.measurements.label(D,ee)
cm = ndimage.measurements.center_of_mass(D, L, [1,2])

distance = numpy.sqrt(sum([numpy.absolute((a - b)) ** 2 for a, b in zip(cm[1], cm[0])])) # Distancia euclidiana

    
if __name__ == '__main__':
    
    # Plot e print do resultado
    result1 = sub_img(mars1, mars2)
    plt.interactive(False)
    plt.imshow(result1, 'gray')
    plt.title('Marcadores')
    plt.axis('off')
    plt.show()
    print('Distancia entre os pontos: ',distance)