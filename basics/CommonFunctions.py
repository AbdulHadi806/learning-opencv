import cv2

img = cv2.imread('./assets/soccer_practice.jpg')

# Converting image to grayscale because most algorithms work best with gray scale images

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Blur image

blured_image = cv2.GaussianBlur(img , (3, 3), cv2.BORDER_DEFAULT)


# Edge Cascade. This is used for finding edges. We will be using Canny() here. There are many other methods
canny = cv2.Canny(blured_image, 100, 175)

# Dilating the image
dilated = cv2.dilate(canny, (3, 3), iterations=3)

# Eroding
eroded = cv2.erode(dilated, (7, 7), iterations=3)

# Resize image
resized = cv2.resize(img, (1000, 1000), interpolation=cv2.INTER_AREA) #INTER_AREA is used when downsizeing, INTER_CUBIC is used when increasing size
cv2.imshow('resized', resized)

# croppedImage
cropped = resized[50:100, 100:400]
cv2.imshow('cropped', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()