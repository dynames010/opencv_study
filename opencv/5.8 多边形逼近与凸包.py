# @Time: 2023/1/29 10:19
# @File: 5.8 多边形逼近与凸包.py
'''
逼近方式（DP算法）:以多边形逼近轮廓
AB两点相连，取最远处一点最短距离是否满足阈值T，大于则取该点与AB点分别相连，再取最远点最短距离
API：
approxPolyDP(curve,epsilon,closed)
curve要近似逼近的轮廓
epsilon即DP算法使用的阈值
closed轮廓是否闭合
返回的是一个轮廓的三位矩阵

凸包：把多边形角点相连
API：
cv2.convexHull
'''
import cv2
import numpy as np
#读取图片
img = cv2.imread(r'D:\xzc\python\opencv\hand.jpeg')
#图片转为灰度图
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
thresh,img_binary = cv2.threshold(img_gray,150,255,cv2.THRESH_BINARY)
#img_binary = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,0)
contours, hierarchy = cv2.findContours(img_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
#获取逼近的轮廓，返回一个轮廓
approx = cv2.approxPolyDP(contours[0],5,closed = True)
print(approx)
#绘制轮廓
cv2.drawContours(img,contours,0,(0,0,255),2)
cv2.drawContours(img,[approx],0,(0,255,255),2)  #draw元素使用的是列表

#计算凸包
hull = cv2.convexHull(contours[0])
#画出凸包
cv2.drawContours(img,[hull],0,(255,0,0),2)

cv2.imshow('img',img)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img_binary',img_binary)
#cv2.imshow('img_bijin',img_bijin)
#cv2.imshow('img_test',img_test)
cv2.waitKey()
cv2.destroyAllWindows()