try:
    import Tkinter as tk #python2
except:
    from tkinter import *

import time
rname="aa"
rtype="bb"
startime=time.time()
root = Tk()                     # 创建窗口对象

def opWi():
    global rname,rtype,root
    need='success'
    #geometry(this窗宽，this窗高,左边距离屏幕位置，上边距离屏幕位置)
    root.geometry('800x500+100+50')
    root.title("we can")
    i=0
    #tuple的第1个参数是字体类型，第2个参数是字体大小，第3个参数的可选内容是：bold, italic, underline, overstrike。
    if need=='onload':
        lab1 = Label(root, text="", font=('Times', 50, ''))
        lab2 = Label(root, text="检测到垃圾，正在识别...", font=('Times', 50, ''))
        lab1.pack()
        lab2.pack()

    if need=='success':
            lab1 = Label(root, text="", font=('Times', 5, ''))
            lab2 = Label(root, text="有害垃圾桶：未满载", font=('Times', 40, ''))
            lab3 = Label(root, text="", font=('Times', 20, ''))
            str1="huishou：",rtype
            lab4 = Label(root, text="可回收垃圾桶：满载", font=('Times', 40, ''))
            lab5 = Label(root, text="", font=('Times', 20, ''))
            str2="chuyv：",rname
            lab6 = Label(root, text="厨余垃圾桶：未满载", font=('Times', 40, ''))#yuan lai :number
            lab7 = Label(root, text="", font=('Times', 20, ''))
            lab8 = Label(root, text="其他垃圾桶：未满载", font=('Times', 40, ''))
            lab1.pack()
            lab2.pack()
            lab3.pack()
            lab4.pack()
            lab5.pack()
            lab6.pack()
            lab7.pack()
            lab8.pack()
    nowtime=time.time()
    if nowtime-startime>5:
        rname="sadfasdf"
    print("there is tkin")
    
    root.mainloop
opWi()


