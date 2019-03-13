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

def distanceCamera(knownWidth, focalLength, perWidth):
   return (knownWidth * focalLength) / perWidth

KNOWN_DISTANCE = 24.0

KNOWN_WIDTH = 11.0

image = cv2.imread("images/2ft.png")
marker = find_marker(image)
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH	

