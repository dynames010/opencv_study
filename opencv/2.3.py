# @Time: 2022/12/22 14:25
# @File: 2.3.py
import cv2
import numpy as np

img = np.zeros((480,640,3),np.uint8)
cv2.line(img,(10,20),(300,400),(0,0,255),5,16)
cv2.rectangle(img,(80,100),(380,380),(0,255,0),5,16)#以对角线确认矩形，参数和直线一样
cv2.circle(img,(200,200),50,(0,250,0),6,16) #圆心、半径大小
pts = np.array([(250,100),(150,300),(50,280)],np.int32)#pts多边形，必须是32位
cv2.polylines(img,[pts],True,(0,0,255),5,16)
#填充多边形
#cv2.fillPoly(img,[pts],(0,0,255),5,16)


#text不支持中文，可以用 pillow包
cv2.putText(img,'HELLO opencv',(50,400),cv2.FONT_HERSHEY_COMPLEX,2,[0,0,255])
#axes -> axis
cv2.ellipse(img,(320,240),(100,50),45,0,360,(0,0,255),5,16)       #先画矩形，框住椭圆,(100,50)椭圆的宽高，45度旋转椭圆，0,360控制画多少长度

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()