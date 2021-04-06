import cv2
import time

#PATH = "/home/pi/Desktop/01.英语二导学.mp4"
def starCamara():
    video = cv2.VideoCapture(-1) # -1

    fps = video.get(cv2.CAP_PROP_FPS)

    success, frame = video.read()

    video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

    video.set(cv2.CAP_PROP_FRAME_WIDTH,640)

    #print('%d',fps)
    img_count = 1

    while success and cv2.waitKey(16) & 0xFF != ord('q'):
        #cv2.waitKeyint (100)
        cv2.imshow('player', frame)
        
        success, frame = video.read()
        key = cv2.waitKey(1)
        
        
        print("image capture start!")
        if img_count <= 6:
            cv2.waitKey(4)
            cv2.imwrite("{}.jpg".format(img_count),frame)
            print("screencut success!")
            img_count += 1
        #if img_count > 6:
            #cv2.destroyAllWindows()
            #video.release()
            #return 
starCamara()
