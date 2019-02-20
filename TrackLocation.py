from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2

argParser = argparse.ArgumentParser()
argParser.add_argument("-v", "--video", type=str,
	help="path to input video file")
argParser.add_argument("-t", "--tracker", type=str, default="kcf",
	help="OpenCV object tracker type")
arguements = vars(argParser.parse_args())

(significant, lessor) = cv2.__version__.split(".")[:2]


if int(significant) == 3 and int(lessor) < 3:
	tracker = cv2.Tracker_create(arguements["tracker"].upper())


else:
	
	OPENCV_OBJECT_TRACKERS = {
		"csrt": cv2.TrackerCSRT_create,
		"kcf": cv2.TrackerKCF_create,
		"boosting": cv2.TrackerBoosting_create,
		"mil": cv2.TrackerMIL_create,
		"tld": cv2.TrackerTLD_create,
		"medianflow": cv2.TrackerMedianFlow_create,
		"mosse": cv2.TrackerMOSSE_create
	}

	tracker = OPENCV_OBJECT_TRACKERS[arguements["tracker"]]()

initBB = None