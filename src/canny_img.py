import cv2 as cv
import numpy as np
import os

img = cv.imread(os.path.join(".", "data", "5r.jpg"))

img = cv.Canny(img, 50, 51)

cv.imshow("img", img)
cv.waitKey(0)




