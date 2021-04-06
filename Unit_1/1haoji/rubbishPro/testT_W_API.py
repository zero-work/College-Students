'''
限制：
1.压力传感器需3次测出重量相加大于5  且在开机3秒后，才会触发事件
2.每0.09秒使压力传感器返回一次数据

'''
import _thread
import time
import cv2 as cv
import cv2 
from tkinter import *
import testGUI

#cezhong
from cezhong import Hx711

#C_UP_API
import cam_upload_getAPI

starTime=time.time()

#status of the 
status=0

#测重量
def cezhong(threadName, delay):
    global status
    send = Hx711()
    send.setup()
    sums=0.0
    i=0
    while True:
        sums+=send.start()
        nowTime=time.time()
        if sums>0.6 and nowTime-starTime>3:
            status=1
            time.sleep(1)
            #C_UP_API
            #jsonStr=cam_upload_getAPI.mains()
            #tkin(jsonStr[0]["name"],jsonStr[0]["type"])
            
            testGUI.opWi("有害垃圾","dianchi")
            #print("the true name is:",jsonStr[0]["name"],"\n the true type is:",jsonStr[0]["type"])
            
            
            #print("get goale",threadName)
            
        #per 3 ci clear
        if i >=2:
            i=0
            sums=0
        
        i+=1
    #print("_________")
    #print(send.start())

# 播放视频
def playV(threadName, delay):
    global status
    #starTime=time.time()
    cap = cv.VideoCapture('thev.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', frame) #gray or frame
        if cv.waitKey(1) == ord('q'):
            break
        if status==1:
            break
        #nowTime=time.time()
        #if nowTime-starTime >= 11:
            #break
    cap.release()
    cv.destroyAllWindows()
    #return Initial start .waiting next use
    status=0




# 创建两个线程
try:
   _thread.start_new_thread( playV, ("Thread-1", 2, ) )
   _thread.start_new_thread( cezhong, ("Thread-2", 3, ) )
   #_thread.start_new_thread( print_time, ("Thread-3", 2, ) )
except:
   print ("Error: 无法启动线程")


