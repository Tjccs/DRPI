# -*- coding: utf-8 -*-

from scipy import ndimage
import imageio
import matplotlib.pyplot as plt
import numpy


img = imageio.imread('/home/tjccs/Projects/sat_map3.tif')
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


def elc_no_sat(img):
    """
    Função que devolve o elc da imagem sem saturação
    :param img: a imagem a utilizar
    :return: O elc da imagem
    """
    min_img = abs(float(numpy.min(img)))
    max_img = abs(float(numpy.max(img)))
    low_bound = 0
    high_bound = 255
    img_elc = (img - min_img) * ((high_bound - low_bound) / (max_img - min_img)) + low_bound
    return img_elc


def elc_sat(img):
    """
    Função que devolve o elc com saturação
    :param img: a imagem a utilizar
    :return: O elc da imagem com saturação
    """
    h, r = numpy.histogram(img, bins=256, range=(0, 256))
    c = 0
    d = 255
    lin = dim[0]
    col = dim[1]

    saturation = 2. / 100
    p = h.astype(float) / (lin * col)
    pa = numpy.cumsum(p)

    a1 = float(numpy.count_nonzero(pa <= saturation / 2) - 1)
    b1 = float(numpy.count_nonzero(pa <= (1 - saturation / 2)) - 1)
    elc1 = ((img.astype(float) - a1) * ((d - c) / (b1 - a1)) + c).clip(0, 255)
    return elc1


if __name__ == '__main__':
    plt.interactive(False)
    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    histogram(elc_no_sat(img[:, :, 0]), 'Histograma ELC de r', [1, 0, 0])
    plt.subplot(132);
    histogram(elc_no_sat(img[:, :, 1]), 'Histograma ELC de g', [0, 1, 0])
    plt.subplot(133);
    histogram(elc_no_sat(img[:, :, 2]), 'Histograma ELC de b', [0, 0, 1])

    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    histogram(elc_sat(img[:, :, 0]), 'Histograma ELC de sat. r', [1, 0, 0])
    plt.subplot(132);
    histogram(elc_sat(img[:, :, 1]), 'Histograma ELC de sat. g', [0, 1, 0])
    plt.subplot(133);
    histogram(elc_sat(img[:, :, 2]), 'Histograma ELC de sat. b', [0, 0, 1])

    plt.figure(figsize=(20, 3))
    plt.subplot(131);
    plt.imshow(numpy.uint8(img))
    plt.title('Inicial');
    plt.axis('off')
    plt.subplot(132);
    plt.imshow(numpy.uint8(elc_no_sat(img)))
    plt.title('ELC sem saturacao');
    plt.axis('off')
    plt.subplot(133);

    plt.imshow(numpy.uint8(elc_sat(img)))
    plt.title('ELC com 0.01% de saturação bilateral');
    plt.axis('off')
    plt.show()