#RGB to BINARY


import  cv2
img=cv2.imread('car.jpg',0)
cv2.imshow('gray scale image',img)


ret, bi_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary image',bi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()