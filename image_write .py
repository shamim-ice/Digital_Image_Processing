#image write 

import cv2
img=cv2.imread('car.jpg')
cv2.imshow('original image',img)
cv2.imwrite('output.jpg',img)
cv2.imwrite('output.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()