#__author__: AngelGCL @github

# using matplotlib
import matplotlib.image as img

import math

class imProcessor:
    def runProc(self, image):
        # load image
        # PARAM: image = string of name of image
        # NOTE: has to be a png file
        m = img.imread(image + ".png")
        h, w = m.shape[:2]
        print(w)
        print(h)
        # array that collects values for each pixel
        valarr = []

        for i in range(h):
            for j in range(w):

                # ratio of RGB will be between 0 and 1
                valarr.append([math.ceil(float(m[i][j][0]) * 255), math.ceil(float(m[i][j][1]) * 255), math.ceil(float(m[i][j][2]) * 255)])
        print(valarr)
        return valarr

    runProc(self=None, image='logo')