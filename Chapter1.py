import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)


img = cv2.imread("Lionel_Messi.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(img, (7,7), 0)

imgCanny = cv2.Canny(img, 100,100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=5)
imgEroded = cv2.erode(imgDilation, kernel, iterations=5)



cv2.imshow("grayImage", imgGray)
cv2.imshow("Blurred",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Dilation",imgDilation)
cv2.imshow("Eroded",imgEroded)
cv2.waitKey(0)
