import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#read img
img = cv.imread("data/5r.jpg")

if img is None:
    print("Missing image file")
    exit()

#configure the face detector using the download .tflite model
base_options = python.BaseOptions(model_asset_path='blaze_face_short_range.tflite')
options = vision.FaceDetectorOptions(base_options=base_options, min_detection_confidence=0.5)



with vision.FaceDetector.create_from_options(options) as detector:
   #convert opencv image to mediapipe
   mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv.cvtColor(img, cv.COLOR_BGR2RGB))
   detection_result = detector.detect(mp_image)

   #draw bounding box if detecting faces

   if detection_result.detections:
       for detection in detection_result.detections:
           bbox = detection.bounding_box

           #draw rectangle using coords
           cv.rectangle(img, (bbox.origin_x, bbox.origin_y), (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height), (0, 255, 255), 2)


cv.imshow("frame", img)
cv.waitKey(0)
cv.destroyAllWindows()
