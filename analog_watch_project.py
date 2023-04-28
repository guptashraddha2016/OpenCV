import cv2
import numpy as np
CANVAS_SIZE = (640,640,3)
image = np.zeros(CANVAS_SIZE, dtype=np.uint8)
#Turn it to white color
image[:] = [255,255,255]

cv2.imshow("winname",image)
cv2.waitKey(0)