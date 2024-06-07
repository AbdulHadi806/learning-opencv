import cv2
import numpy as np

img = cv2.resize(cv2.imread('./assets/dog.jpg'), (0, 0), fx=0.5, fy=0.2)

blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

rectangle = cv2.rectangle(blank.copy(), (30, 30),  (img.shape[1]//2, img.shape[0]//2), 255, -1)
cv2.imshow('rectangle', rectangle)

weird_shape = cv2.bitwise_and(circle, rectangle) 
cv2.imshow('Maks', weird_shape)


masked = cv2.bitwise_and(img, img, mask=weird_shape)
cv2.imshow('masked', masked)

cv2.waitKey(0)