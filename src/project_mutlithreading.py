import numpy as np
import cv2
import threading
import datetime
a = datetime.datetime.now()
video_capture_0=cv2.VideoCapture(0)
video_capture_1=cv2.VideoCapture(2)
def cam1():
    while True:

        ret0, frame0 = video_capture_0.read()
        if(ret0):
            cv2.imshow('Cam0',frame0)

def cam2():
    while True:

        ret1, frame1 = video_capture_1.read()
        if(ret1):
            cv2.imshow('Cam1',frame1)
t1=threading.Thread(target=cam1)
t2=threading.Thread(target=cam2)
while True:

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

t1.start()
t2.start()



video_capture_0.release()
video_capture_1.release()

cv2.destroyAllWindows()

