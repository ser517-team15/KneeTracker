import sys

pathx = 'C:/Users/Abhishek/Anaconda4/envs/opencv-env';
sys.path.append(pathx)

import numpy as np
import cv2

import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5065

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
# print "message:", MESSAGE

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
