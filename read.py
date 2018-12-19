import numpy as np

import cv2

imgpath = './img/people1.png'
# read an image
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
print(img)
print(img.shape)

# make a image window resizable
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# display an color image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destoryAllWindows()

