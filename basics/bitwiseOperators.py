import cv2
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200) , 200, 255, -1)

cv2.imshow('Rectangle', rectangle)
cv2.imshow('circle', circle)


# bitwise AND --> Finds intersecting regions
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow('bitwise_and', bitwise_and)

# bitwise OR --> Finds none intersecting and intersacting regions
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow('bitwise_or', bitwise_or)

# bitwise XOR --> Finds none intersecting regions
bitwise_xor= cv2.bitwise_xor(rectangle, circle)
cv2.imshow('bitwise_xor', bitwise_xor)

# bitwise NOT --> It converts 1 to 0 and 0 to 1 i.e black region to white and white to black
bitwise_not= cv2.bitwise_not(circle)
cv2.imshow('bitwise_not', bitwise_not)

cv2.waitKey(0)