import cv2
import os

#read image
image_path = os.path.join(".", "data", "5r.jpg")

img = cv2.imread(image_path)

print(img.shape)

#write image

cv2.imwrite(os.path.join(".", "data", "5r_out.jpg"), img)

#visualize image

cv2.imshow("Me", img)
cv2.waitKey(0)
