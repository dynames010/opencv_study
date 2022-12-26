# @Time: 2022/12/18 21:19
# @File: 1.7trackbar使用.py
import cv2
import numpy as np
cv2.namedWindow('trackbar',cv2.WINDOW_NORMAL)
cv2.resizeWindow('trackbar',640,480)

#定义回调函数
def callback(value):
    print(value)

#创建三个trackbar
print(cv2.createTrackbar('R','trackbar',0,255,callback))
cv2.createTrackbar('G','trackbar',0,255,callback)
cv2.createTrackbar('B','trackbar',0,255,callback)

#创建背景图
img = np.zeros((480,640,3),np.uint8)

while True:
    cv2.imshow('trackbar',img)
    #获取当前trackbar的值
    r = cv2.getTrackbarPos('R','trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    img[:]=[b,g,r]
    key = cv2.waitKey(1)

cv2.destroyAllWindow()