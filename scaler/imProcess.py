#__author__: AngelGCL @github
# using numpy
import numpy as npy

# using matplotlib
import matplotlib.image as img

# using statistics to import median
# for median calculation
from statistics import median

import math

class imProcessor:
    #load image
    m = img.imread("logo.png")
    # determining width and height of original image
    h, w = m.shape[:2]
    print(w)
    print(h)
    #iterator for statistical purposes
    ite = 0
    #array that collects median values for each pixel
    subarr = []
    #array that collects median values for each specified amount of rows
    suparr = []
    for i in range(h):
        for j in range(w):

            # ratio of RGB will be between 0 and 1
            lst = [float(m[i][j][0]), float(m[i][j][1]), float(m[i][j][2])]

            mediana = float(median(lst))
            subarr.append(mediana)
            ite+=1
            if ite == 9152: #0.01639344262295081967213114754098 percent of the whole data
                suparr.append(math.floor(((median(subarr) * 21) % 255)) + 21)
                ite = 0
                subarr = []
    print(suparr)