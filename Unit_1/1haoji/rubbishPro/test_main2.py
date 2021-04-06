'''
流程：
→视频
→V内创建新体重检测进程
→创建识别垃圾进程，等待视频的关闭才开始运行
→修改窗口值，调用舵机投放；结束后修改状态值，打开视频
→视频
'''

from tkinter import *

import time
import _thread
import cv2 as cv
#C_UP_API
import cam_upload_getAPI

from cezhong import Hx711

import test_toufang


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
def newData(xing1,xing2):
    global tizhongSta
    global rtype,rname
    while True:
        #if videoSta==0:
        #print("tizhongSta is:",tizhongSta)
            #time.sleep(0.2)
            #continue
        if tizhongSta==1:
            print("***********************************")
            jsonReturn=cam_upload_getAPI.mains()
            getName=jsonReturn[0]["name"]
            getType=jsonReturn[0]["type"]
            print("(",getType,")")
            #cnames.set("changed")
            rtype=getType
            rname=getName
            print("change")
            tizhongSta=2 #API OK ,next tou fang
            #videoSta=0
            #getAPISta=1
            print("in newData take turn videoSta=0 getAPISta=1")
            #break

# 播放视频
def playV(threadName, delay):
    global tizhongSta,star_Vd_Ce
    #starTime=time.time()
    while True:
        if tizhongSta==0:
            if star_Vd_Ce>=1:
                time.sleep(5)
            cap = cv.VideoCapture('/home/pi/Desktop/rubbishPro/thev.mp4')
            while cap.isOpened():
                ret,frame = cap.read()
                cv.namedWindow('frame',0)
                cv.resizeWindow('frame',1000,580)
                cv.imshow('frame',frame)
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                if cv.waitKey(1) == ord('q'):
                    break
                if tizhongSta==1:
                    star_Vd_Ce+=1;
                    break
                #nowTime=time.time()
                #if nowTime-starTime >= 11:
                    #break
            cap.release()
            cv.destroyAllWindows()
            print("video to close,")
    
    

#监测重量
def cezhong(xing1,xing2):
    global tizhongSta,startime,star_Vd_Ce
    send = Hx711()#创建测体重类的成员
    send.setup()
    sums=0.0
    i=0
    while True:
        if tizhongSta==0:
            if(star_Vd_Ce==2):
                time.sleep(5)
                star_Vd_Ce=1
            weight=send.start()
            sums+=weight
            
            nowTime=time.time()
            if sums>0.75 and nowTime-startime>5:
                print("get goale;",weight)
                sums=0.0
                tizhongSta=1
                
                print("in cezhong take turn tizhongSta=1 ")
            if i >=2:
                i=0
                sums=0
            i+=1
            #print("_________")
            #print(send.start())
    
#垃圾投放分类
def rubbishTou(rtype):
    print("rype is",rtype)
    
    #re.match('com', 'www.runoob.com')
    #if rtype==" 厨余垃圾 ":
        
    
    if re.match(rtype,'有害垃圾')!=None:
        test_toufang.send_ser(0)
        print("there is 0 send")
        
    if re.match(rtype,'可回收垃圾')!=None:
        test_toufang.send_ser(90)
        print("there is 90 send")
        
    if re.match(rtype,'厨余垃圾')!=None:
        test_toufang.send_ser(180)
        print("there is 180 send") 
        
    if re.match(rtype,'其他垃圾')!=None:
        test_toufang.send_ser(270)
        print("there is 270 send")
    time.sleep(3)
    test_toufang.recv()
    print(test_toufang.buffer)
    
        
        
        
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
        if tizhongSta==2:
            ltype.set("垃圾类别："+rtype)
            lname.set("垃圾名字："+rname)
            print("change the label!")
            
            rubbishTou(rtype)
            
            star_Vd_Ce=2
            #in there or after in toufang
            tizhongSta=0
            
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
        _thread.start_new_thread( cezhong, ("Thread-1", 2, ) )
    except:
       print ("Error: 无法启动线程cezhong")
    #GUI
    opWi()
    test_toufang.send_ser(666)
    recv()
    print(test_toufang.buffer)
    #time.sleep(3)
    

mains()