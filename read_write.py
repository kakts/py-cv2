import numpy as np
import sys
import cv2


args = sys.argv
if len(args) != 2:
  raise Exception('args len should be 2. Please set the imgName')
imgName = args[1]
ext = '.png'

fileName = imgName + ext
print(imgName)
img = cv2.imread('./img/' + fileName, cv2.IMREAD_COLOR)
print(img)
cv2.imwrite('./saved_img/' + fileName, img)