import cv2

image = cv2.imread('nature.jpg',cv2.IMREAD_COLOR)

image1 = cv2.imread('nature.jpg',cv2.IMREAD_GRAYSCALE)
width = 500
height = 300

dsize = (width, height)
output = cv2.resize(image, dsize)

cv2.imshow("window",output)
cv2.waitKey(0)