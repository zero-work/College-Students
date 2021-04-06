from cezhong import Hx711
send = Hx711()
send.setup()
sums=0.0
i=0
while True:
    weight=send.start()
    print("weight:",weight)
    sums+=weight
    
    if sums>0.7:
        print("get goale;",weight)
    if i >=2:
        i=0
        sums=0
    i+=1
    #print("_________")
    #print(send.start())
    
