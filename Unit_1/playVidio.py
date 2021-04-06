import numpy as np
import cv2 as cv
import time


def playVideo():
    starTime=time.time()

    cap = cv.VideoCapture('thev.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame)#gray or frame
        if cv.waitKey(1) == ord('q'):
            break
        nowTime=time.time()
        #if nowTime-starTime >= 6:
            #break
    cap.release()
    cv.destroyAllWindows()
