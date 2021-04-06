# -*- coding: utf-8 -*
import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 115200)
if ser.isOpen == False:
    ser.open             # 打开串口
# ser.write(b"ready")
# time.sleep(10)
ser.write(b"666")
# time.sleep(10)
# ser.write(b"2()   70")
# time.sleep(10)
# ser.write(b"0")
try:
    while True:
        size = ser.inWaiting()
        #symbol = ser.read_until("flag")# 获得缓冲区字符
       # ser.write(b"270")
        if size != 0:
            response = ser.read(ser.inWaiting())        # 读取内容并显示
            print (response)
           # if symbol == "flag":
                
               # startcamera()
                
            time.sleep(0.1)               # 软件延时
except KeyboardInterrupt:
    ser.close()
