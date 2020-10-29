import cv2
import numpy as np
img = cv2.imread("Lionel_Messi.jpg")
print(img.shape)
# (720, 1280,3) here 720 is height, 1280 is width and 3 is no of channel RGB ##
imgResize = cv2.resize(img, (800, 500))   ## here first is width and second is height

imgCropped = img[100:350, 100:600]   ## here first is height and second is width ##

cv2.imshow("original",img)
cv2.imshow("imgResize",imgResize)
cv2.imshow("imgCropped",imgCropped)
cv2.waitKey(0)