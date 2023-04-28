import cv2
import numpy as np

image = cv2.imread("nature.jpg")


# translation matrix 
matrix = np.float32([[1,0,100],[0,1,100]])

#applying the matrix to the image

translated = cv2.warpAffine(image,matrix,(image.shape[1]+100,image.shape[0]+100))

cv2.imshow("orignal",image)
cv2.imshow("translate",translated)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()