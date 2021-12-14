#Image edge detection

import cv2
import numpy as np
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.waitKey(0)
height,width=img.shape[:2]
sobel_x=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
cv2.imshow('Sobel_x image',sobel_x)
cv2.waitKey(0)
sobel_y=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
cv2.imshow('sobel_y image',sobel_y)
cv2.waitKey(0)
sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('sobel_or image',sobel_or)
cv2.waitKey(0)
laplacian=cv2.Laplacian(img,cv2.CV_8U)
cv2.imshow('Laplacian image',laplacian)
cv2.waitKey(0)
canny=cv2.Canny(img,100,200)
cv2.imshow('Canny image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()