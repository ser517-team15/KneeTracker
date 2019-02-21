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

if not arguements.get("video", False):
	print("Starting Camera.....")
	videoFrame = VideoStream(src=0).start()
	time.sleep(1.0)

else:
	videoFrame = cv2.VideoCapture(arguements["video"])

framePerSecond = None

while True:

	currentFrame = videoFrame.read()
	currentFrame = currentFrame[1] if arguements.get("video", False) else currentFrame

	if currentFrame is None:
		break


	currentFrame = imutils.resize(currentFrame, width=1000, height=500)
	(H, W) = currentFrame.shape[:2]

	if initialize is not None:
		(success, box) = realTimeTracker.update(currentFrame)
		if success:
			(x, y, w, h) = [int(v) for v in box]
			cv2.rectangle(currentFrame, (x, y), (x + w, y + h),
						  (0, 255, 0), 2)

		framePerSecond.update()
		framePerSecond.stop()

		display_Screen = [
			("Tracker", arguements["tracker"]),
			("Success", "Yes" if success else "No"),
			("FPS", "{:.2f}".format(framePerSecond.fps())),
		]
		
		for (i, (k, v)) in enumerate(display_Screen):
			text = "{}: {}".format(k, v)
			cv2.putText(currentFrame, text, (10, H - ((i * 20) + 20)),
						cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

	cv2.imshow("Frame", currentFrame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("s"):
		initialize = cv2.selectROI("Frame", currentFrame, fromCenter=False,
								   showCrosshair=True)


		realTimeTracker.init(currentFrame, initialize)
		framePerSecond = FPS().start()

	elif key == ord("q"):
		break
