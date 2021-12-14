#Image Arithmatic

import cv2
import numpy as np
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.waitKey(0)
M=np.ones(img.shape ,dtype='uint8')*150
add=cv2.add(img,M)
cv2.imshow('added image',add)
cv2.waitKey(0)
subtract=cv2.subtract(img,M)
cv2.imshow('subtracted image',subtract)
cv2.waitKey(0)
multiply=cv2.multiply(img,M)
cv2.imshow('multiply image',multiply)
cv2.waitKey(0)
cv2.destroyAllWindows()