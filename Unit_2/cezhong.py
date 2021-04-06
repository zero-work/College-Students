# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


class Hx711:
    def setup(self):
        self.SCK = 12  # 物理引脚第12号，时钟
        self.DT = 13  # 物理引脚第13号，数据
        self.flag = 1  # 用于首次读数校准
        self.initweight = 0
        self.weight = 0
        self.delay = 0.09
        # self.count=[0,0,0,0]
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
        GPIO.setup(self.SCK, GPIO.OUT)  # Set pin's mode is output
        GPIO.setup(self.DT, GPIO.IN)
        GPIO.setup(self.DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self) -> float:
        GPIO.output(self.SCK, 0)
        if GPIO.input(self.SCK):
            time.sleep(self.delay)
            # self.count[0]+=1
        value = 0
        while GPIO.input(self.DT):
            time.sleep(self.delay)
            # self.count[1]+=1
        for i in range(24):
            GPIO.output(self.SCK, 1)
            if (0 == GPIO.input(self.SCK)):
                time.sleep(self.delay)
                # self.count[2]+=1
            value = value << 1  # 左移一位，相当于乘2
            GPIO.output(self.SCK, 0)
            if GPIO.input(self.SCK):
                time.sleep(self.delay)
                # self.count[3]+=1
            if GPIO.input(self.DT) == 1:
                value += 1
        GPIO.output(self.SCK, 1)
        GPIO.output(self.SCK, 0)
        value = int(value / 405)  # 405为我传感器的特性值，不同传感器值不同。可先注释此步骤，再去测一物体A得到一个值X,而后用X除以A的真实值即可确定特性值
        if self.flag == 1:
            self.flag = 0
            self.initweight = value  # 初始值
            return float(value)
        else:
            self.weight = abs(value - self.initweight)  # 当前值减初始值得测量到的重量
            real_w=round((self.weight/1000), 5)
            print(real_w)
            return float(real_w)
            # self.count=[0,0,0,0]


if __name__ == '__main__':
    send = Hx711()
    send.setup()
    while True:
        send.start()


