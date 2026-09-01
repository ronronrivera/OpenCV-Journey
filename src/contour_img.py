import os
import cv2 as cv

img = cv.imread(os.path.join(".", "data", "5r.jpg"))

img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv.contourArea(cnt) > 200:
        cv.drawContours(img, cnt, -1,(0, 255, 0), 1)

cv.imshow("thresh", img)
cv.waitKey(0)

