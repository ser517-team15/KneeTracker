#! /usr/bin/env python

import cv2 as cav
import numpy as np
from math import *
import time

cap = cav.VideoCapture('video.3gp')
fourcc = cav.VideoWriter_fourcc('M', 'J', 'P', 'G')
writer = cav.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))

# ball tracking class
class BallClass:
    ballPosition = {'x': 0, 'y': 0, 'r': 0}
    distance = 0.0

    countFit = 0

    distanceThreshold = 15
    repeatThreshold = 3

    def positionSetter(self, x, y, r):
        newDistance = sqrt(pow(x, 2) + pow(y, 2))
        if abs(self.distance - newDistance) < self.distanceThreshold:
            self.countFit += 1
            print 'addFit'
        else:
            self.countFit = 0
            print 'resetFit'

        # update position
        self.distance = newDistance
        self.ballPosition['x'], self.ballPosition['y'], self.ballPosition['r'] = x, y, r

        # is over limit
        if self.countFit > self.repeatThreshold:
            return True
        else:
            return False


ball = BallClass()

tracker = None

while (True):
    ret, frame = cap.read()

    if ret:
        startTime = time.time()

        scale = 0.5

        inputImg = cav.resize(frame, (0, 0), fx=scale, fy=scale)

        HSVImg = cav.cvtColor(inputImg, cav.COLOR_RGB2HSV)

        thresholdImg = cav.inRange(HSVImg[:, :, 0], 104, 112)

        blurImg = cav.blur(thresholdImg, (7, 7))

        circles = cav.HoughCircles(blurImg, cav.HOUGH_GRADIENT, 2, 20, param1=400, param2=90)

        blurImg = cav.cvtColor(blurImg, cav.COLOR_GRAY2BGR)

        # draw circles
        if circles is not None:
            for (x, y, r) in circles[0, :]:
                if ball.positionSetter(x, y, r):
                    # update tracker
                    del tracker
                    tracker = cav.TrackerKCF_create()
                    ok = tracker.init(inputImg, (int(x - r), int(y - r), int(r * 2), int(r * 2)))

                    cav.rectangle(HSVImg, (int(x - r), int(y - r)), (int(x + r), int(y + r)),
                                  (200, 200, 200), 5, 1)

                cav.circle(blurImg, (x, y), r, (200, 200, 200), 5)

        # if not ballFit:
        if tracker:
            ok, roi = tracker.update(inputImg)
            tracker.clear()
            if ok:
                p1 = (int(roi[0]), int(roi[1]))
                p2 = (int(roi[0]) + int(roi[2]), int(roi[1]) + int(roi[3]))
                cav.rectangle(inputImg, p1, p2, (0, 200, 200), 5, 1)

        # hsvv = HSVImg[:, :, 0]
        h, s, v = cav.split(HSVImg)
        hsvvn = cav.cvtColor(h, cav.COLOR_GRAY2BGR)

        imccn1 = np.concatenate((inputImg, HSVImg), axis=1)
        imccn2 = np.concatenate((hsvvn, blurImg), axis=1)
        imccn3 = np.concatenate((imccn1, imccn2), axis=0)

        cav.imshow('imgOut', imccn3)

        writer.write(imccn3)
        cav.waitKey(1)

        endTime = time.time()
        print 'time:', endTime - startTime

    else:
        break

cap.release()
writer.release()