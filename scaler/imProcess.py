# using numpy
import numpy as npy

# using matplotlib
import matplotlib.image as img

# using statistics to import mean
# for mean calculation
from statistics import mean, median

import math

m = img.imread("logo.png")
# determining width and height of original image
h, w = m.shape[:2]

newImage = npy.zeros([h, w, 3])
print(w)
print(h)
ite = 0
subarr = []
suparr = []
for i in range(h):
    for j in range(w):

        # ratio of RGB will be between 0 and 1
        lst = [float(m[i][j][0]), float(m[i][j][1]), float(m[i][j][2])]
        #print(math.floor(((median(subarr) * 21) % 255)) + 21)

        mediana = float(median(lst))
        subarr.append(mediana)
        ite+=1
        if ite == 9152:
            suparr.append(math.floor(((median(subarr) * 21) % 255)) + 21)
            ite = 0
            subarr = []

print(suparr)
# Save image using imsave
#img.imsave('grayedImage.png', newImage)