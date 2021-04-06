# -*- coding: utf-8 -*
import serial
import time
#huan chong qu
buffer=""
def send_ser(degree):
    ser = serial.Serial('/dev/ttyAMA0', 115200)
    if ser.isOpen == False:
        ser.open()                # 打开串口
    if degree==0:
        ser.write(b"0")
        print("turn 0")
    if degree==90:
        ser.write(b"90")
        print("turn 90")
    if degree==180:
        ser.write(b"180")
        print("turn 180")
    if degree==270:
        ser.write(b"270")
        print("turn 270")
    #recv()
    ser.close()

def recv():
    try:
        while True:
            size = ser.inWaiting()               # 获得缓冲区字符
            if size != 0:
                response = ser.readline(size)        # 读取内容并显示
                #print (response)
                buff = response
                ser.flushInput()                 # 清空接收缓存区
                time.sleep(0.1)               # 软件延时
    except KeyboardInterrupt:
        ser.close()

