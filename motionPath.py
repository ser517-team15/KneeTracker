
import argparse
import time
import cv2

aparse = argparse.ArgumentParser()
aparse.add_argument("v", "video", help="path of video")
aparse.add_argument("m-a", "min-area", type=int, default=500, help="minimum area")
args = vars(aparse.parse_args())

if args.get("video", None) is None:
    vs = VideoStream(src=0).start()
    time.sleep(3.0)

else:
    vs = cv2.VideoCapture(args["video"])

firstFrame = None