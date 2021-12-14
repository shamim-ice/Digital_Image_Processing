#image pyramid

import cv2
import numpy as np
img=cv2.imread('car.jpg')
smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)
cv2.imshow('original image',img)

cv2.waitKey(0)
cv2.imshow('smaller image',smaller)
cv2.waitKey(0)
cv2.imshow('larger image',larger)
cv2.waitKey(0)
cv2.destroyAllWindows()