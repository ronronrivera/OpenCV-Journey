import cv2
import os


img = cv2.imread(os.path.join(".", "data", "5r.jpg"))



#resize img
img = cv2.resize(img, (640, 480))

print(img.shape)


cv2.imshow("img", img)
cv2.waitKey(0)
