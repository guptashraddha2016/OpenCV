import cv2
import numpy as np

canvas = np.zeros((500,500,3))

#required points to join
pts = np.array([[250,5],[220,80],[280,80],[100,100]], np.int32)

#Reshape the points to shape (number, vertex 1,2)
pts = pts.reshape((-1,1,2))

cv2.polylines(canvas,[pts],True,(0,255,0),3)

cv2.imshow("winname",canvas)
cv2.waitKey(0)