'''
流程：
→视频
→V内创建新体重检测进程
→创建识别垃圾进程，等待视频的关闭才开始运行
→修改窗口值，调用舵机投放；结束后修改状态值，打开视频
→视频
'''

from time import sleep
from tkinter import *
import serial
import time
import _thread
import cv2
#C_UP_API
import cam_upload_getAPI

from cezhong import Hx711

import test_one_bo

import Toufang


startime=time.time()

needAPI='success'

rtype="识别ing.."
rname="识别ing.."

root = Tk()                     # 创建窗口对象
lname = StringVar()  #
lname.set("垃圾名字："+rname)
ltype = StringVar()
ltype.set("垃圾类别："+rtype)



tizhongSta=0 ##0:播放视频，监听体重  1:关闭视频，关闭体重检测
  #2:不调用API  3：调用API   一次
    #4：不更新GUI  5：更新GUI

star_Vd_Ce=0

#获取API的zhi

# 播放视频
def playV(threadName, delay):
    global tizhongSta
    #starTime=time.time()
    while True:
        if tizhongSta==0:
            time.sleep(5)
            cap = cv2.VideoCapture('thev.mp4')
            cv2.namedWindow("frame",0)
            cv2.moveWindow("frame",300,200)
            cv2.resizeWindow("frame",960,540)
            while cap.isOpened():
                ret, frame = cap.read()
                # if frame is read correctly ret is True
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame', frame)#gray or frame
                
                if cv2.waitKey(1) == ord('q'):
                    break
                if tizhongSta==1:
                    tizhongSta = 2
                    break
                #nowTime=time.time()
                #if nowTime-starTime >= 11:
                    #break
            cap.release()
            cv2.destroyAllWindows()
            print("video to close,")       

#监测重量
            
def uart(xing1,xing2):
    global tizhongSta,startime,star_Vd_Ce
    i=0
    ser = serial.Serial('/dev/ttyAMA0', 115200)
    if(ser.isOpen==False):
        ser.open()
    while True:
        size = ser.inWaiting()
        
        buff = ser.read(size)
        if buff == b'666\r\n':
            print(buff)
            tizhongSta = 1            
#             nowTime=time.time()
#             if test_one_bo.spend()=="geted" and nowTime-startime>5:
#                 print("get goale;",weight)
#                 tizhongSta=1
#                 print("in cezhong take turn tizhongSta=1 ")
#             i+=1    
            
def newData(xing1,xing2):
    global tizhongSta
    global rtype,rname
    while True:
        #if videoSta==0:
        #print("tizhongSta is:",tizhongSta)
            #time.sleep(0.2)
            #continue
        
        if tizhongSta==3:
            print("***********************************")
            jsonReturn=cam_upload_getAPI.mains()
            getName=jsonReturn[0]["name"]
            getType=jsonReturn[0]["type"]
            print("(",getType,")")
            #cnames.set("changed")
            rtype=getType
            rname=getName
            print(rtype)
            print("change")
            tizhongSta=4 #API OK ,next tou fang
            #videoSta=0
            #getAPISta=1
            print("in newData take turn videoSta=0 getAPISta=1")
        else:
            time.sleep(0.1)
            #break
            
#垃圾投放分类
def rubbishTou(rtype):
    print("rype is",rtype)
    if re.match(rtype,'有害垃圾')!=None:
        Toufang.send_degree(0)
        print("there is 0 send")
        
    if re.match(rtype,"可回收垃圾")!=None:
        Toufang.send_degree(90)
        print("there is 90 send")
        
    if re.match(rtype,"厨余垃圾")!=None:
        Toufang.send_degree(180)
        print("there is 180 send") 
        
    if re.match(rtype,"其他垃圾")!=None:
        Toufang.send_degree(270)
        print("there is 270 send")
        

#windows
def opWi():
    global needAPI,rname,rtype,root
    global lname,ltype,tizhongSta
    #geometry(this窗宽，this窗高,左边距离屏幕位置，上边距离屏幕位置)
    root.geometry('800x500+100+50')
    root.title("we can")
    root.configure(bg='black')
    
    #tuple的第1个参数是字体类型，第2个参数是字体大小，第3个参数的可选内容是：bold, italic, underline, overstrike。
    if needAPI=='onload':
        lab1 = Label(root, text="", font=('Times', 50, ''))
        lab2 = Label(root, text="检测到垃圾，正在识别...", font=('Times', 50, ''))
        lab1.pack()
        lab2.pack()

    if needAPI=='success':
            lab1 = Label(root, text="", font=('Times', 20, ''))
            lab2 = Label(root, text="  序  号：   1    ", font=('Times', 50, ''),fg="white")
            lab3 = Label(root, text="", font=('Times', 20, ''))

            lab4 = Label(root, textvariable= lname, font=('Times', 50, ''),fg="white")
            lab5 = Label(root, text="", font=('Times', 20, ''))

            lab6 = Label(root, textvariable = ltype, font=('Times', 50, ''),fg="white")#yuan lai :number
            lab7 = Label(root, text="", font=('Times', 20, ''))
            lab8 = Label(root, text="分类情况：待 分 类", font=('Times', 50, ''),fg="white")
            
            lab2.configure(bg='black')
            lab4.configure(bg='black')
            lab6.configure(bg='black')
            lab8.configure(bg='black')
            
            lab1.pack()
            lab2.pack()
            lab3.pack()
            lab4.pack()
            lab5.pack()
            lab6.pack()
            lab7.pack()
            lab8.pack()
    #root.mainloop()
    while True:
        #if getAPISta==0:
            #print("updata label in waiting ")
        if tizhongSta==4:
            ltype.set("垃圾类别："+rtype)
            lname.set("垃圾名字："+rname)
            tizhongSta=0
        if tizhongSta==2:
            ltype.set("垃圾类别：识别中...")
            lname.set("垃圾名字：识别中...")
            print("change the label!")    
            star_Vd_Ce=2
            #in there or after in toufang
            tizhongSta=3
            print("in opWi take turn tizhongSta=0")
        root.update()
        #print("there is tkin")
    
def mains():
    global rname,rtype,labName
    print("ones")
    try:
        #video
        _thread.start_new_thread( playV, ("Thread-1", 2, ) )
    except:
       print ("Error: 无法启动线程video")
       
    try:
        #newData
        _thread.start_new_thread( newData, ("Thread-1", 2, ) )
    except:
       print ("Error: 无法启动线程newData")
    try:
        #newData
        _thread.start_new_thread( uart, ("Thread-1", 2, ) )
    except:
       print ("Error: 无法启动线程cezhong")
    #GUI
    opWi()
    
    
    #time.sleep(3)
    

mains()
