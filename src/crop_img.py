import os
import cv2

img = cv2.imread(os.path.join(".", "data", "5r.jpg"))


#crop
cropped_img = img[320:640, 480:840]

print(img.shape)

cv2.imshow("frame", img)
cv2.imshow("frame", cropped_img)

cv2.waitKey(0)
