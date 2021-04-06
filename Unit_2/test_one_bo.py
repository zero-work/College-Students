# -*- coding: utf-8 -*
import serial
import time
def spend():
    ser = serial.Serial('/dev/ttyAMA0', 115200)
    if ser.isOpen == False:
        ser.open()                # 打开串口

    try:
        while True:
            size = ser.inWaiting()
            #symbol = ser.read_until("flag")# 获得缓冲区字符
            if size != 0:
                response = ser.read(ser.inWaiting())        # 读取内容并显示
                #get respond 
                if response==b'1\r\n':
                   return "geted"
                   #print("get info is '1\r\n'")
                print(response)
                time.sleep(0.1)               # 软件延时
    except KeyboardInterrupt:
        ser.close()

