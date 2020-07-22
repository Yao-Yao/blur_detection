import cv2

fname='example.jpg'
cv2.namedWindow('imageWindow')
img = cv2.imread(fname)
cv2.imshow('imageWindow',img)
cv2.waitKey()
