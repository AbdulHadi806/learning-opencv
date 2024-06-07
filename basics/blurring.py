# methods for blurring
import cv2

img = cv2.imread('./assets/soccer_practice.jpg')

average = cv2.blur(img, (3, 3))
cv2.imshow('blur', average)

gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('blur2', gauss)

# median blur is used to reduce noise
median = cv2.medianBlur(img, 3)
cv2.imshow('median', median)

# Bilateral blurring is most effective and is used in big computer vision projects. Remaining algos blur image ignoring the edges, etc. This is not the
# case with this algo

bilateral = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)