import cv2
import numpy as np

img = cv2.resize(cv2.imread('./assets/dog.jpg'), (0, 0), fx=0.5, fy=0.2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Laplacian Edge Detection method
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap", lap)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combine_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("Combined Sobel", combine_sobel)

canny = cv2.Canny(gray, 150, 175)
cv2.imshow("canny", canny)

print(cv2.CV_64F, 'cv2.CV_64F')

cv2.waitKey(0)