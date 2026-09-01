import cv2 as cv
import os

img = cv.imread(os.path.join(".", "data", "5r.jpg"))

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#ret, thresh = cv.threshold(img, 80, 255, cv.THRESH_BINARY)
thresh = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 30)

cv.imshow("pic", thresh)
cv.waitKey(0)
