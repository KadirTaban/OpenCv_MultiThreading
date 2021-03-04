import numpy as np
import cv2
import datetime
a = datetime.datetime.now()
video_capture_0=cv2.VideoCapture(0)
path = "video.mp4"
video_capture_1 = cv2.VideoCapture(path)

while True:
    ret0, frame0= video_capture_0.read()
    ret1, frame1 = video_capture_1.read()

    if(ret0):
        b = datetime.datetime.now()
        print(b - a)

        cv2.imshow('Cam0',frame0)

    if(ret1):
        cv2.imshow('Cam1',frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture_0.release()
video_capture_1.release()


cv2.destroyAllWindows()
