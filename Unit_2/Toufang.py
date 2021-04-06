import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 115200)
if ser.isOpen == False:
    ser.open()                # 打开串口
def send_degree(degree):
    size = ser.inWaiting()
    #symbol = ser.read_until("flag")# 获得缓冲区字符
    if size != 0:
        respon = ser.read(size)
        print(respon)# 读取内容并显示
        if respon == b'666\r\n':
            if degree==0:
                ser.write(b'0')
                print("turn 0")
            if degree==90:
                ser.write(b'90')
                print("turn 90")
            if degree==180:
                ser.write(b'180')
                print("turn 180")
            if degree==270:
                ser.write(b'270')
                print("turn 270")
    ser.flush()
    time.sleep(0.1)
