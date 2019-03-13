from imutils import paths
import numpy as np
import imutils
import cv2

def find_marker(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	contoursDetected = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	contoursDetected = imutils.grab_contours(contoursDetected)
	c = max(contoursDetected, key = cv2.contourArea)

	return cv2.minAreaRect(c)

