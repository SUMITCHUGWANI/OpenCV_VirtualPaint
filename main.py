# This is a sample Python script.
import cv2
print("pacakage Installed")
## HERE OUTPUT IS THE SCREEN NAME
#
# img = cv2.imread("Lionel_Messi.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)


# cap = cv2.VideoCapture("video.mkv")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(10) & 0xFF == ord('s'):
#         break
    # if cv2.waitKey(10) & 0xFF == ord('s'):
    #     break

cap = cv2.VideoCapture(0)
cap.set(3, 640)   ## for length of screen
cap.set(4, 480)   ## for bredth of screen
cap.set(10,100)   ## for brightness

while True:
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break



