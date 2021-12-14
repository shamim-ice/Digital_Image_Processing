#get image info

import cv2
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
print(img.shape)
print('Height pixel values',img.shape[0])
print('Width pixel values',img.shape[1])
print('layer of image',img.shape[2])
cv2.waitKey(0)
cv2.destroyAllWindows()