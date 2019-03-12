import numpy

#settings the input camera calibration parameters

focal_length = 942.8
dist_betn_lenses = 54.8
disparities = 64
block = 15
units = 0.001

for x in range(block, left.shape[0] - block - 1):
    for y in range(block + disparities, left.shape[1] - block - 1):
        differences = numpy.empty([disparities, 1])

        l = left[(x - block):(x + block), (y - block):(y + block)]
        for d in range(0, disparities):
            r = right[(x - block):(x + block), (y - d - block):(y - d + block)]
            differences[d] = numpy.sum((l[:, :] - r[:, :]) ** 2)

        disparity[x, y] = numpy.argmin(differences)

depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (focal_length * dist_betn_lenses) / (units * disparity[disparity > 0])