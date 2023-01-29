# @Time: 2023/1/29 16:02
# @File: 5.9 最大最小外接矩形.py
'''
minAreaRect(points)最小外接矩阵
points为轮廓，返回元组，内容是旋转矩形的参数
boundingRect(points)最大外接矩形
最大外接矩形不会旋转，故只返回xywh参数
'''
import cv2
import numpy as np

#读取图片
img = cv2.imread(r'D:\xzc\python\opencv\hand.jpeg')
#图片转为灰度图
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
thresh,img_binary = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(img_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#最小矩形轮廓
rect = cv2.minAreaRect(contours[0])
#寻找旋转矩形并且画出矩形，计算出四个坐标点
box = cv2.boxPoints(rect)
print(box)
box = np.around(box).astype('int')  #通过Np方法画出最小矩阵

#最大矩形轮廓，返回最大外接矩形参数，xy wh
x,y,w,h = cv2.boundingRect(contours[0])
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.drawContours(img,[box],0,(0,255,0),2)   #box值需要为整数

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()