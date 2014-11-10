import cv2
import numpy as np

## image processing algorithm based on QI Xiaorui, 
## MA Lei, LIU Jiang, and SUN Changjiang, "Fast Skew Angle
## Detection Algorithm for Scanned Document Images"

## import test image (development purposes only)
test = cv2.imread("perfecttext.jpg")
test2 = cv2.imread("perfecttextwithimage.jpg")


kernel = np.uint8(np.ones((2,2)))
kernelbig = np.uint8(np.ones((5,5)))


## step 1: convert to black and white

## accidentally combined many steps into one big function for now
def convertToBW(img):
	bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## sobel derivative (in x direction):
	sobel = cv2.Sobel(bw, cv2.CV_8U, 1, 0, ksize=1)

##	threshold image:
	ret, thresh = cv2.threshold(sobel, 150, 255, cv2.THRESH_BINARY)

## erode and then dilate, to remove noise
	eroded = cv2.erode(thresh, kernel, iterations=1)
	dilated = cv2.dilate(eroded, kernelbig, iterations=4)


	return dilated

## step 2: horizontal gradient

## step 3: merge text areas

## step 4: filter text areas

## step 5: filter non-text areas

## step 6: identify lines


img = convertToBW(test2)


#show image (development purposes only)
window = cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()