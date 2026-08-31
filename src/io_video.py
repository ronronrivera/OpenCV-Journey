import os
import cv2

#read video
video_path = os.path.join(".", "data", "t.mp4")

video = cv2.VideoCapture(video_path)

#visualize video

ret = True

while ret:
    ret, frame = video.read()
    
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

#release memory
video.release()
cv2.destroyAllWindows()
