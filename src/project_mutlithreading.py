
import numpy as np
import cv2
import threading
import datetime
a=datetime.datetime.now()
def function_1():
    video_capture_0 = cv2.VideoCapture(0)

    while True:
        ret0,frame0=video_capture_0.read()
        if(ret0):
            b=datetime.datetime.now()
            cv2.imshow("cam0",frame0)
            if cv2.waitKey(34) & 0xFF == ord('q'):
                break
        else:
            break
    video_capture_0.release()
    cv2.destroyAllWindows()


def function_2():

    video_capture_1 = cv2.VideoCapture("http://192.168.1.103:4747/video")

    while True:
        ret1,frame1=video_capture_1.read()
        if(ret1):
            cv2.imshow("cam1",frame1)
            if cv2.waitKey(34) & 0xFF == ord('q'):
                break
        else:
            break
    video_capture_1.release()
    cv2.destroyAllWindows()


t1=threading.Thread(target=function_1)
t2=threading.Thread(target=function_2)

t1.start()
t2.start()
t1.join()
t2.join()