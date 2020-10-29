import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
# img[:] = 0,255,0   ## to color the box
# img[200:300,100:300] = 0,0,255
print(img.shape)

cv2.line(img,(0,0),(410,470), (111, 189, 269), 3)
cv2.line(img,(0,0),(img.shape[1], img.shape[0]),(214,79,255),3)
cv2.rectangle(img, (0,0),(378,391), (200,247,91),3)
cv2.rectangle(img, (512,512), (300,300),(140,25,101),cv2.FILLED)
cv2.circle(img, (350,150),10, (240,140,49),4)
cv2.putText(img, "OPENCV",(40,80),cv2.FONT_HERSHEY_TRIPLEX,2, (0,0,255), 5)




cv2.imshow("Img",img)

cv2.waitKey(0)


### WARP PERSPECTIVE


width, height = 250,350

img1 = cv2.imread("PlayingCards.jpg")
pts1 = np.float32([[228,91],[431,136],[164,381],[369,426]])

## points should be matching with the pts 2 (1,2,3,4)
pts2 = np.float32([[0,0],[width,0],[0,height],[width, height]])



matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img1, matrix, (width, height))


cv2.imshow("Output", imgOutput)
cv2.waitKey(0 )



## JOining Images

img_joker = cv2.imread("cards.jpg")
imgHor = np.hstack((img_joker,img_joker))
imgVer = np.vstack((img_joker,img_joker))

## we can not add gray with color images, dimensions should be equal

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)
