# -*- coding: utf-8 -*
import serial
import time


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
    
    ser.close()
buff =""
def recv():
    try:
        ser.write(b"1dsd")
        while True:
            size = ser.inWaiting()               # 获得缓冲区字符
            if size != 0:
                global buff
                response = ser.read(size)
                # 读取内容并显示
                buff = response
                print (response)       
                ser.flushInput()                 # 清空接收缓存区
                time.sleep(0.1)               # 软件延时
    except KeyboardInterrupt:
        ser.close()

