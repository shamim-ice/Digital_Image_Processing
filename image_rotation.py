#image rotation

import cv2
import numpy as np
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.waitKey(0)
height,width=img.shape[:2]
rotation_matrix=cv2.getRotationMatrix2D((width/2,height/2),70,.5)
rotated_img=cv2.warpAffine(img,rotation_matrix,(width,height))
cv2.imshow('roted image',rotated_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
