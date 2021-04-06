# -*- coding: utf-8 -*
import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 115200)
if ser.isOpen == False:
    ser.open()                # 打开串口
try:
    while True:
        size = ser.inWaiting()
        #symbol = ser.read_until("flag")# 获得缓冲区字符
        if size != 0:
            response = ser.read(ser.inWaiting())        # 读取内容并显示
            print (response)
            if response == "1\r\n":
                print("1\r\n")
                #startcamera()
            if response == "1":
                print("2")
            time.sleep(0.1)               # 软件延时
except KeyboardInterrupt:
    ser.close()

