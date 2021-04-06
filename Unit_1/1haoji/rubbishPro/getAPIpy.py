import json
import requests
import base64
#import time


#startTime=time.time();

#将图片转为
def imgTObase():
    with open('6.jpg', 'rb') as f:  # 以二进制读取图片
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        #print(encodestr)  # 重新编码数据
    return encodestr
    

#调用垃圾分类API
def toRubbishAPI():
    url = 'http://api.tianapi.com/txapi/imglajifenlei/'

    # encode = base64.b64encode(imgdata) #imgdata根据你的程序获取图片数据流后进行base64编码处理
    body = {
        "key": "497e254c36c2efe672634a54bb326b2f",
        "img": imgTObase()
    }
    headers = {'content-type': "application/x-www-form-urlencoded"}
    
    
    
    response = requests.post(url, data=body, headers=headers)

    # 返回信息 is String of type
    strs=response.text
    #print(strs)
    jsonStr = json.loads(strs)
    
    print(jsonStr["newslist"])
    print(type(jsonStr))

#startFun=time.time()-startTime;
#print("the startFun:",startFun)

toRubbishAPI()
    
    


    

