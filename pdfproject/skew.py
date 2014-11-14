import numpy as np
import cv2

# rotate an image by a given angle
def rotate(img, angle):
	height, width = img.shape
	rotmat = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
	return cv2.warpAffine(img, rotmat, (width, height))

# get the sum of the values of a row
def horizontal_sums(img):
	height, width = img.shape
	sums = []
	for i in range(0+height/4, height-height/4, (height/50)):
		sums.append(sum(img[i]))
	return sums

# rotate an image by an angle that maximizes the standard deviation of its row sums
def straighten(input_img):
	img = np.copy(input_img)
	if len(img.shape) > 2:
		img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

	img = np.uint8(img)
	img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 10)

	stds = {}

	# this can be done recurisively, and to greater precision
	# but this works for now
	for x in range(-90, 90, 5):
		stds[np.std(horizontal_sums(rotate(img, x)))] = x
	angle = stds[max(stds.keys())]
	for i in range(angle-10, angle+10):
		stds[np.std(horizontal_sums(rotate(img, i)))] = i
	angle = stds[max(stds.keys())]
	
	return rotate(input_img, angle)
