#image Translation

import cv2;
import numpy as np
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.waitKey(0)

#store height and width

height,width=img.shape[:2]
print(height)
print(width)
quarter_height=height/4;
quarter_width=width/4;
print(quarter_height)
print(quarter_width)

#T is our translation matrix

T=np.float32([[1,0,quarter_width],[0,1,quarter_height]])
print(T)

translation_img=cv2.warpAffine(img,T,(width,height))
cv2.imshow('translation image',translation_img)
cv2.waitKey(0)
cv2.destroyAllWindows()