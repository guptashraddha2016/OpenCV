import cv2
import numpy as np

#scaling image

#original image
image = cv2.imread("nature.jpg")

#resize 
image = cv2.resize(image,(300,300))

#resizing image using linear interploation
image_linear  = cv2.resize(image,(500,500),fx=5.5, fy=5.5, interpolation=cv2.INTER_LINEAR)

image_qubic  = cv2.resize(image,(500,500),fx=5.5, fy=5.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow("original",image)
cv2.imshow("linear",image_linear)
cv2.imshow("qubic",image_qubic)
if cv2.waitKey()==ord('q'):
    cv2.destroyAllWindows()