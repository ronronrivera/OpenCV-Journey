import os
import cv2 as cv


img = cv.imread(os.path.join(".", "data", "5r.jpg"))

k_size = 11

#img = cv.blur(img, (k_size, k_size))
#img = cv.GaussianBlur(img, (k_size, k_size), 3)
img = cv.medianBlur(img, k_size)

cv.imshow("image", img)
cv.waitKey(0)
