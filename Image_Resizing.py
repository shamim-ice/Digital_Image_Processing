#Image Resizing

import cv2
import numpy as np
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.waitKey(0)

#lets make the size of our image 3/4 of it's original image

image_scaled=cv2.resize(img,None,fx=0.75,fy=0.75)
cv2.imshow('Scaling linear interpolation',image_scaled)
cv2.waitKey(0)

#lets make the size of our image 2 of it's original image

image_scaled2=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('Scaling cubic interpolation',image_scaled2)
cv2.waitKey(0)

image_scaled3=cv2.resize(img,(600,400),interpolation=cv2.INTER_AREA)
cv2.imshow('Scaling skewed image',image_scaled3)
cv2.waitKey(0)
cv2.destroyAllWindows()
