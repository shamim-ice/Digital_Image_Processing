import cv2
import numpy as np

img = cv2.imread('car.jpg')
"""
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 500)
height = int(img.shape[0] * scale_percent / 500)
dim = (width, height)
img2 = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
"""

cv2.imshow('orignal image', img)
cv2.waitKey(0)

R,G,B = cv2.split(img)
zeros = np.zeros(img.shape[:2],dtype = 'uint8')

cv2.imshow('Red', cv2.merge([zeros, zeros, R]))
cv2.waitKey(0)

cv2.imshow('Green', cv2.merge([zeros, G, zeros]))
cv2.waitKey(0)

cv2.imshow('Blue', cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)

cv2.destroyAllWindows()
