import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#read img

#configure the face detector using the download .tflite model
base_options = python.BaseOptions(model_asset_path='blaze_face_short_range.tflite')
options = vision.FaceDetectorOptions(base_options=base_options, min_detection_confidence=0.5)


cam = cv.VideoCapture(0)

if not cam.isOpened():
    print("Could not open webcam")
    exit()



with vision.FaceDetector.create_from_options(options) as detector:
   #convert opencv image to mediapipe
   while True:
       #Get the frame height and width to prevent out of bounds error
       frame_height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
       frame_width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))

       ret, frame = cam.read()

       #conver frame to RGB
       rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
       mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

       #Run face detection
       detection_result = detector.detect(mp_image)

       if detection_result.detections:
           for detection in detection_result.detections:
               bbox = detection.bounding_box

               #safely confined coordinates within the frame bounds
               y1 = max(0, bbox.origin_y)
               x1 = max(0, bbox.origin_x)

               y2 = min(frame_height, bbox.origin_y + bbox.height)
               x2 = min(frame_width, bbox.origin_x + bbox.width)

               #check if the face slices is valid and not empty

               if (y2 - y1)>0 and (x2 - x1) > 0:
                   #face region
                   face = frame[y1:y2, x1:x2]

                   #blur effect
                   blurred_face = cv.blur(face, (50, 50))

                   frame[y1:y2, x1:x2] = blurred_face


       cv.imshow("cam", frame)
       if cv.waitKey(1) & 0xFF == ord('q'):
           break


#clean up and close all windows safely
cam.release()
cv.destroyAllWindows()


