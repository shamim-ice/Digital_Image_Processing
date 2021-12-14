"""
RGB to HSV
H=hue(0-180)
S=saturation(=0-255)
V=value(0-255)
"""

import cv2;
img=cv2.imread('car.jpg')
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image',hsv_img)
cv2.imshow('hue channel',hsv_img[:,:,0])
cv2.imshow('saturation channel',hsv_img[:,:,1])
cv2.imshow('value channel',hsv_img[:,:,2])


cv2.waitKey(0)
cv2.destroyAllWindows()