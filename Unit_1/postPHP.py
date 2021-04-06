import json
import requests

def send_file():
    url = 'https://test.yanbixing123.com/DEMO17/forPys.php'
    files = {'file1': open('1.jpg', 'rb'),'file2': open('2.jpg', 'rb'),'file3': open('3.jpg', 'rb')}                         
    data = {'test':'all','key2':'value2'}
    
    response = requests.post(url, files=files, data=data)
    #json = response.json()#but the return type is String!
    #print(json,'\n')
    return response


#getResponse = send_requests1()
getResponse = send_file()
strs=getResponse.text.encode('latin-1').decode('unicode_escape')
status=getResponse.status_code #if the status is 200,to request success!
print ('------ getResponse.text = ',strs,status)
    
    
    