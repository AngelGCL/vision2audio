#__author__: AngelGCL @github
# using numpy
import numpy as npy

# using matplotlib
import matplotlib.image as img

# using statistics to import median
# for median calculation
from statistics import median, mean

import math

class imProcessor:
    #load image
    m = img.imread("logo.png")
    # determining width and height of original image
    h, w = m.shape[:2]
    print(w)
    print(h)
    #time = (float(0.1 * 255) /4) % 60
    #print(time)
    #iterator for statistical purposes
    ite = 0
    #array that collects median values for each pixel
    arrR = []
    arrG = []
    arrB = []
    #array that collects median values for each specified amount of rows
    suparr = []
    for i in range(h):
        for j in range(w):

            # ratio of RGB will be between 0 and 1
            #lst = [, , ]
            arrB.append(float(m[i][j][0]))
            arrG.append(float(m[i][j][1]))
            arrR.append(float(m[i][j][2]))

            #media = float(mean(lst))
            #subarr.append(media)
            ite+=1
            if ite == 9152: #0.01639344262295081967213114754098 percent of the whole data
            #NOTE: floor((rgb value * 255 max in color values) MOD 21 due to min in note scale being 21)
            # + 21 because for zero value, note should be 21
                note = math.floor(((mean(arrR) * 255) % 21)) + 21
            # NOTE: add 1 to prevent zero value and multiply (1/8) so that the
            # smallest duration is a beat of 1/8 of a second
                duration = (math.ceil(((mean(arrB) * 255) % 21)) + 1) * (1/8)
            #NOTE: Volume of the note is taken from the G value and 50 is added so that
            # when it is lower than 50 it will have a higher value so it can be heard
                volume = math.floor(((mean(arrG) * 255) % 127))
                if volume < 50: volume += 50
                suparr.append([note, duration, volume])
                ite = 0
                arrB = []
                arrR = []
                arrG = []
    print(suparr)