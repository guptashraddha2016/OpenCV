import cv2
import numpy as np

image = cv2.imread("sample.jpg")

height, width= image.shape[:2]

#translation matrix 
matrix = cv2.getRotationMatrix2D((width/2,height/2),20,2)

#applying the matrix to the image
translated = cv2.warpAffine(image,matrix,(width,height))

#showing the image
cv2.imshow("translation",translated)
cv2.waitKey(0)