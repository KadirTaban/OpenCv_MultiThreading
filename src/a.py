import numpy as np
import cv2
import time
import threading
def webcam_video():

  cap = cv2.VideoCapture(0)
  while(True):
    ret, frame = cap.read()
    if ret == True:
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else :
        break
  cap.release()
  cv2.destroyAllWindows()

def local_video():

  cap = cv2.VideoCapture(2)
  while(True):
    ret, frame = cap.read()
    if ret == True:
     cv2.imshow('frame_2',frame)
     if cv2.waitKey(1) & 0xFF == ord('x'):
        break
    else :
        break
  cap.release()



p1= threading.Thread(target = local_video)
p2= threading.Thread(target = webcam_video)
p1.start()

p2.start()

