import numpy
import cv2

fx = 942.8
depth_betn_lens = 54.8
disparities = 128
block = 31
units = 0.001

output = cv2.StereoBM_create(numDisparities=disparities,
                             blockSize=block)

disparity = output.compute(left, right)

depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (fx * depth_betn_lens) / (units * disparity[disparity > 0])