import cv2
import numpy as np

img = cv2.imread("sample.jpg")

kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3 = np.ones((3,3),dtype=np.float32)/9.0
kernel_11 = np.ones((11,11),dtype=np.float32)/121.0


# print(kernel_identity)
# print(kernel_3)
# print(kernel_11)

# apply the filters
output1 = cv2.filter2D(img,-1,kernel_identity)
output2 = cv2.filter2D(img,-1,kernel_3)
output3 = cv2.filter2D(img,-1,kernel_11)

cv2.imshow("orignal",img)
cv2.imshow("kernel_identity",output1)
cv2.imshow("kernel_3",output2)
cv2.imshow("kernel_11",output3)
cv2.waitKey(0)