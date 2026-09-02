import cv2 as cv
import numpy as np

from PIL import Image
from utils import get_limits


black = [0, 255, 255]

cap = cv.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_limit, upper_limit = get_limits(color=black)

    mask = cv.inRange(hsvImage, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    print(bbox)

    #show webcam
    cv.imshow("frame", frame)

    if cv.waitKey(40) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()
