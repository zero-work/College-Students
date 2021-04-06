#test get php array
import json
import requests
import cv2
import time

#camera
def starCamera():
    video = cv2.VideoCapture(-1)

    fps = video.get(cv2.CAP_PROP_FPS)

    success, frame = video.read()

    video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    video.set(cv2.CAP_PROP_FRAME_WIDTH,640)

    #print('%d',fps)
    img_count = 1
    
    #read success  AND (not put Q (key) and )
    while success and cv2.waitKey(16) & 0xFF != ord('q'):
        #cv2.waitKeyint (100)
        cv2.imshow('player', frame)
        
        success, frame = video.read()
        key = cv2.waitKey(1)

        print("image capture start!")
        if img_count <= 6:
        
            cv2.imwrite("{}.jpg".format(img_count),frame)
            print("screencut success!")
            img_count += 1
        if img_count > 6:
            #turn off the windows
            cv2.destroyAllWindows()
            video.release()
            return 


#send post of the text format
def send_requests1():
    url = 'https://test.yanbixing123.com/DEMO17/givePyArray.php'
    d = {'test': 'I am from py', 'key2': 'value2'}
    r = requests.post(url, data=d)
    return r

def send_file():
    url = 'https://test.yanbixing123.com/DEMO17/forPys.php'
    files = {'file1': open('6.jpg', 'rb')}
    #files = {'file1': open('4.jpg', 'rb'),'file2': open('5.jpg', 'rb'),'file3': open('6.jpg', 'rb')}              
    data = {'key1':'img1.jpg','test':'all'}
    
    response = requests.post(url, files=files, data=data)
    #json = response.json()#but the return type is String!
    #print(json,'\n')
    return response

#count the Precision
def countPre(jsonStr):
    realDate={}
    if(jsonStr["0"]["name"]==jsonStr["1"]["name"]):
        realDate["name"]=jsonStr["0"]["name"]
        realDate["type"]=jsonStr["0"]["type"]
    if(jsonStr["0"]["name"]==jsonStr["2"]["name"]):
        realDate["name"]=jsonStr["0"]["name"]
        realDate["type"]=jsonStr["0"]["type"]
    if(jsonStr["1"]["name"]==jsonStr["2"]["name"]):
        realDate["name"]=jsonStr["1"]["name"]
        realDate["type"]=jsonStr["1"]["type"]
    return realDate
    
def mains():
    #use camera for get image
    
    starCamera()

    #send request 
    #getResponse = send_requests1()
    getResponse = send_file()
    strs=getResponse.text.encode('latin-1').decode('unicode_escape')

    status=getResponse.status_code #if the status is 200,to request success!
    print(strs)
    jsonStr = json.loads(strs)

    #realDate=countPre(jsonStr)
    #__print("the true name is:",jsonStr[0]["name"],"\n the true type is:",jsonStr[0]["type"])
    #print("the true name is:",realDate["name"],"\n the true type is:",realDate["type"])

    print ('------ getResponse.text = ',strs,status)
    return jsonStr

