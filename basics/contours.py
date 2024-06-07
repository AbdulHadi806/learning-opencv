import cv2
import numpy as np

img = cv2.resize(cv2.imread("./assets/dog.jpg"), (0, 0), fx=0.3, fy=0.2)
blank = np.zeros(img.shape, dtype="uint8")
cv2.imshow('blank', blank)

cv2.imshow("Cats", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny edges', canny)


contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # CHAIN_APPROX_NONE

print(len(contours))

drawn_image = cv2.drawContours(blank, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=2)
cv2.imshow('drawn_image', drawn_image)

cv2.waitKey(0)