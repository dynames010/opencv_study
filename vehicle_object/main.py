# @Time: 2023/2/18 15:18
# @File: main.py
'''
车辆项目：画出车辆框线，根据大小筛选，划线，统计车辆数目
'''

import cv2
import numpy as np
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

line_height = 700
cap = cv2.VideoCapture(r'D:\xzc\python\opencv\车辆识别.mp4')

#前后景分割提取
mog  = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

#设置识别的最小车型的大小
min_w = 60
min_h = 100
max_w = 20
max_h = 20
vehicle_count = 0

#偏移量
offset = 6

#计算外接矩形中心点
def center(x,y,w,h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = int(x) + x1
    cy = int(y) + y1
    return cx,cy

#循环读取视频
while True:
    ret,frame = cap.read()
    cv2.line(frame, (10,line_height),(1800,line_height),(255,255,0),3)
    if ret == True:
        #把原始帧灰度化，再去噪
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #去噪,高斯滤波
        blur = cv2.GaussianBlur(gray,(3,3),5)
        #比较出画面前后动静的差别
        fgmask = mog.apply(blur)

        #腐蚀
        erode = cv2.erode(fgmask,kernel)
        #膨胀,还原图像
        dialte = cv2.dilate(erode,kernel,iterations=2)

        #消除内部小块
        #闭运算
        close = cv2.morphologyEx(dialte,cv2.MORPH_CLOSE,kernel)
        cv2.imshow('test', close)
        #查找轮廓,注意返回值顺序
        contours,result = cv2.findContours(close,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #画出所有检测出的轮廓
        #cv2.drawContours(frame, contours, 0, (0, 0, 255), 2)
        for contour in contours:
            #最大外接矩形
            (x,y,w,h) = cv2.boundingRect(contour)
            cx,cy = center(x, y, w, h)
            #print('宽{0},高{1}'.format(w,h))
            #通过外接矩形宽高来过滤小矩形
            is_valid = (w >= min_w) & (h >= min_h)
            if not is_valid:
                continue
            #坐标点都是整数,注意绘制矩形函数用法！！！！
            #画一个圆，标记中心点
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            cv2.rectangle(frame, (int(x),int(y)),(int(x+w),int(y+h)),(0,0,255),2)
            if cy>(line_height-offset) and cy<(line_height+offset):
                vehicle_count += 1
                print(vehicle_count)
        cv2.imshow('video', frame)

    key =cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()