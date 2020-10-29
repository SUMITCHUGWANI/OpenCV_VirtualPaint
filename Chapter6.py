import cv2

faceCascade = cv2.CascadeClassifier("face.xml")
img = cv2.imread("face.jpg")

imgResize = cv2.resize(img, (500,800))

faces = faceCascade.detectMultiScale(imgResize, 1.1,4)   ## scale factor = 1.1, minimum neighbour = 4 can be changed depending upon result ##

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize, (x,y),(x+w, y+h),(255,0,0),2)

cv2.imshow("img",imgResize)
cv2.waitKey(0)