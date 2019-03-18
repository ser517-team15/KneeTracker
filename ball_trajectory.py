import cv2
import numpy as np

"""
params = dict(dp=1,
              minDist=1,
              circles=None,
              param1=30,
              param2=15,
              minRadius=1,
              maxRadius=100)
"""

img = np.ones((200,250,3), dtype=np.uint8)
for i in range(50, 80, 1):
    for j in range(40, 70, 1):
        img[i][j]*=200

cv2.circle(img, (120,120), 20, (100,200,80), -1)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 200, 300)

cv2.imshow('subtracted_ball', canny)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1, 20,
              param1=100,
              param2=30,
              minRadius=0,
              maxRadius=0)

print circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('circles', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()