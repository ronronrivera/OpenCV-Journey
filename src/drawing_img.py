import cv2 as cv
import os

img = cv.imread(os.path.join(".", "data", "5r.jpg"))

#line
cv.line(img, (100, 150), (0, 0), (0, 255, 0), 3)

#rectangle
cv.rectangle(img, (200, 350), (450, 600), (0,0,255), 5)

#circle
cv.circle(img, (400, 1000), 120, (0, 140, 255), 10)


#text
cv.putText(img, "Hello!", (800, 400), cv.FONT_HERSHEY_SIMPLEX, 50, (255, 0, 255), 10)

cv.imshow("img", img)
cv.waitKey(0)
