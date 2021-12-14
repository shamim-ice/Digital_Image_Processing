#Image cropping

import cv2
import numpy as np
img=cv2.imread('car.jpg')
height,width=img.shape[:2]
st_row=int(height*.25)
st_col=int(width*.25)
ed_row=int(height*.75)
ed_col=int(width*.75)
cropped=img[st_row:ed_row,st_col:ed_col]
cv2.imshow('original image',img)
cv2.waitKey(0)
cv2.imshow('cropped image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()