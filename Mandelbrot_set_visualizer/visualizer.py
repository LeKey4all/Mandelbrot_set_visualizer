from PIL import Image
import colorsys
import math
import os

from coloringAlgos import powerColor, logColor

#pixels
pic_width = 1000
x = -0.65
y = 0.0
xRange = 3.4
aspectRatio = 4/3
#max iterations to determine diversion:
precision = 500

pic_height = round(pic_width / aspectRatio)
yRange = xRange / aspectRatio
minX = x - xRange / 2
maxX = x + xRange / 2
minY = y - yRange / 2
maxY = y + yRange / 2
progress = 1

img = Image.new('RGB', (pic_width, pic_height), color='black')
pixels = img.load()

for row in range(pic_height):
    for col in range(pic_width):
        x = minX + col + xRange / pic_width
        y = maxY - row * yRange / pic_height
        oldX = x
        oldY = y

        for i in range(precision+1):
            a = x*x - y*y   #real part of z^2
            b = 2*x*y       #imaginary part of z^2
            x = a + oldX
            y = b + oldY
            progress = i
            #if point diverges break:
            if x*x + y*y > 4:
                break

        #compute the pixel value with the advancement in percision threshold
        if progress < precision:
            distance = (progress + 1) / (precision + 1)
            rgb = powerColor(distance, 0.2, 0.27, 1)
            pixels[col, row] = rgb

#img.save('Output.png')
img.show()







