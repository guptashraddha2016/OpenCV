#image
#point
#color
#thickness
#line type

import cv2
import numpy as np

canvas = np.zeros((500,500,3))

print(canvas)

# line type ---- 3 types - Line 4(codrapal), Line 8(octa) , Line AA (anti alise)
# antialiasing reduce the transparancy of pixels
#Algorithm used - Line 4 and Line 8 - Breshanham Algorithm  ,  Line AA - Gausian Filtering

cv2.line(canvas, (0,0), (100,100),(0,0,0),5,cv2.LINE_4)
cv2.line(canvas, (0,10), (100,100),(0,0,255),5,cv2.LINE_8)

cv2.rectangle(canvas,(100,100),(200,200),(255,0,0),5)
cv2.circle(canvas,(200,250),20,(0,0,255),2)

cv2.arrowedLine(canvas,(400,400),(400,500),(0,255,0),3,cv2.LINE_4, tipLength=0.2)
cv2.imshow("winname",canvas)
cv2.waitKey(0)