from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

argueParser = argparse.ArgumentParser()
argueParser.add_argument("-v", "--video", type=str)
argueParser.add_argument("-t", "--tracker", type=str, default="kcf")
arguements = vars(argueParser.parse_args())


object_Trackers = {
		"csrt": cv2.TrackerCSRT_create,
		"kcf": cv2.TrackerKCF_create,
		"boosting": cv2.TrackerBoosting_create,
		"mil": cv2.TrackerMIL_create,
		"tld": cv2.TrackerTLD_create,
		"medianflow": cv2.TrackerMedianFlow_create,
		"mosse": cv2.TrackerMOSSE_create
	}

realTimeTracker = object_Trackers[arguements["tracker"]]()

initialize = None