# -*- coding: utf-8 -*-

import imageio
import matplotlib.pyplot as plt
import numpy


img = imageio.imread('Z:/DRPI/questoes_aula/sat_map3.tif')
dim = img.shape
col = dim[1]
lin = dim[0]


def histogram(img, s, rgb):
    """
    Função que desenha os histogramas
    :param img: A imagem
    :param s: A legenda
    :param rgb: A cor pretendida
    :return: O histograma
    """
    hs = plt.hist(img.ravel(), bins = 256, range=(0, 255), color= rgb, histtype = 'step')
    helc = hs[0]
    plt.title(s, fontsize = 10)
    return helc


def elc_no_saturation(img):
    """
    Função que devolve o elc da imagem sem saturação
    :param img: a imagem a utilizar
    :return: O elc da imagem
    """
    min_img = abs(float(numpy.min(img)))
    max_img = abs(float(numpy.max(img)))
    lower_threshhold = 0
    higher_threshhold = 255
    elc_result = (img - min_img) * ((higher_threshhold - lower_threshhold) / (max_img - min_img)) + lower_threshhold
    return elc_result


def elc_saturation(img):
    """
    Função que devolve o elc com saturação
    :param img: a imagem a utilizar
    :return: O elc da imagem com saturação
    """
    h, r = numpy.histogram(img, bins=256, range=(0, 256))
    c = 0
    d = 255
    
    saturation = 2.0 / 100
    p = h.astype(float) / (lin * col)
    pa = numpy.cumsum(p)
    
    a1 = float(numpy.count_nonzero(pa <= saturation / 2) - 1)
    b1 = float(numpy.count_nonzero(pa <= (1 - saturation / 2)) - 1)
    elc_sat_final = ((img.astype(float) - a1) * ((d - c) / (b1 - a1)) + c).clip(0, 255)
    
    return elc_sat_final

def equalization(img):
    """
    Função que equaliza o histograma
    :param img: a imagem a aplicar a equalização
    :return: O histograma equalizado
    """
    h,r = numpy.histogram(img, bins=256, range=(0, 256))
    p = h/float(dim[0] * dim[1])
    pa = numpy.cumsum(p)
    pa_norm = pa*255
    equ = numpy.zeros((lin,col, dim[2]))
    for i in range(len(pa_norm)):
        equ = equ+(img==i)*int(pa_norm[i])
    
    return equ

def equalization_2(img):
    """
    Função que equaliza o histograma
    :param img: a imagem a aplicar a equalização
    :return: O histograma equalizado
    """
    h,r = numpy.histogram(img, bins=256, range=(0, 256))
    p = h/float(lin * col)
    pa = numpy.cumsum(p)
    pa_norm = pa*255
    eq = numpy.zeros((lin,col))
    for i in range(len(pa_norm)):
        eq = eq+(img==i)*int(pa_norm[i])
    
    return numpy.cumsum(h), eq

if __name__ == '__main__':
    # ------------------ Exercicio 1 ----------------------------- #
    
    # Plot dos Histogramas ELC
    plt.interactive(False)
    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    histogram(elc_no_saturation(img[:, :, 0]), 'Histograma ELC de r', [1, 0, 0])
    plt.subplot(132);
    histogram(elc_no_saturation(img[:, :, 1]), 'Histograma ELC de g', [0, 1, 0])
    plt.subplot(133);
    histogram(elc_no_saturation(img[:, :, 2]), 'Histograma ELC de b', [0, 0, 1])

    # Plot dos histogramas ELC saturados
    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    histogram(elc_saturation(img[:, :, 0]), 'Histograma ELC de sat. r', [1, 0, 0])
    plt.subplot(132);
    histogram(elc_saturation(img[:, :, 1]), 'Histograma ELC de sat. g', [0, 1, 0])
    plt.subplot(133);
    histogram(elc_saturation(img[:, :, 2]), 'Histograma ELC de sat. b', [0, 0, 1])

    # Plot das imagens
    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    plt.imshow(numpy.uint8(img))
    plt.title('Inicial');
    plt.axis('off')
    plt.subplot(132);
    plt.imshow(numpy.uint8(elc_no_saturation(img)))
    plt.title('ELC sem saturacao');
    plt.axis('off')
    
    plt.subplot(133);plt.imshow(numpy.uint8(elc_saturation(img)), 'gray')
    plt.title('ELC com 0.01% de saturação bilateral');
    plt.axis('off')
    plt.show()
    
    # ------------------ Exercicio 2 ----------------------------- #
    
    # Plot dos histogramas não equalizados
    plt.figure(figsize=(20, 3))
    plt.subplot(141);histogram(img[:,:,0], 'Histograma de r', [1,0,0])
    plt.subplot(142);histogram(img[:,:,1], 'Histograma de g', [0,1,0]) 
    plt.subplot(143);histogram(img[:,:,2], 'Histograma de b', [0,0,1]) 
    
    # Plot dos histogramas acumulados
    plt.figure(figsize=(20, 3))
    plt.subplot(141);plt.plot(equalization_2(img[:,:,0])[0], color = 'r')
    plt.title('acumulado hist de r')
    plt.subplot(142);plt.plot(equalization_2(img[:,:,1])[0], color = 'g')
    plt.title('acumulado hist de g')
    plt.subplot(143);plt.plot(equalization_2(img[:,:,2])[0], color = 'b')
    plt.title('acumulado hist de b')
    
    # Plot dos histogramas equalizados
    plt.figure(figsize=(20, 3))
    plt.subplot(141);red = histogram(equalization_2(img[:,:,0])[1],'Hist equalizado r',[1,0,0])
    plt.subplot(142);green = histogram(equalization_2(img[:,:,0])[1],'Hist equalizado g',[0,1,0])
    plt.subplot(143);blue = histogram(equalization_2(img[:,:,0])[1],'Hist equalizado b',[0,0,1])
        
    # Plot dos histogramas acumulados a partir do seu equalizado
    plt.figure(figsize=(20, 3))
    plt.subplot(141);plt.plot(numpy.cumsum(red), color = 'r')
    plt.title('acumulado do equal. de r')
    plt.subplot(142);plt.plot(numpy.cumsum(green), color = 'g')
    plt.title('acumulado do equal. de g')
    plt.subplot(143);plt.plot(numpy.cumsum(blue), color = 'b')
    plt.title('acumulado do equal. de b')
    
    # Plot das imagens
    plt.figure(figsize=(20, 2))
    plt.subplot(141); plt.imshow(numpy.uint8(img))
    plt.title('Inicial'); plt.axis('off')
    plt.subplot(142); plt.imshow(numpy.uint8(equalization(img)), 'gray')
    plt.title('Imagem equalizada'); plt.axis('off')
    plt.show()