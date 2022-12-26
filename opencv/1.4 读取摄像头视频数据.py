# @Time: 2022/12/18 19:57
# @File: 1.4 读取摄像头视频数据.py
import cv2

cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 1920, 1080)

cap = cv2.VideoCapture(r'D:\xzc\Overwatch 2022.05.11 - 19.10.41.03.DVR.mp4')

#循环读取摄像头每一帧
while True:
    #读一帧数据，返回标记，True表示读到标记和一帧数据
    ret,frame = cap.read()
    if not ret:
        print('fail to read video')
        break
    #显示数据
    cv2.imshow('video',frame)
    #一个视频是30帧,没长图片间隔1000/30
    key = cv2.waitKey(1000//30)   #等待10ms，只能填入整数
    if key == ord('q'):
        break
#释放资源
cap.release()
cv2.destroyAllWindows()
