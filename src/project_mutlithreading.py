import numpy as np
import cv2
import threading
import datetime
video_capture_1=cv2.VideoCapture(1)
video_capture_0 = cv2.VideoCapture(0)
def function_1():

    while True:
        ret0,frame0=video_capture_0.read()
        if(ret0):
            cv2.imshow("cam0",frame0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def function_2():

    while True:
        ret1,frame1=video_capture_1.read()
        if(ret1):
            cv2.imshow("cam1",frame1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

t1=threading.Thread(target=function_1)
t2=threading.Thread(target=function_2)

t2.start()
t1.start()
video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()