# @Time: 2023/1/28 16:00
# @File: 5.7 图像轮廓.py
#findCountours
'''
mode
RETR_LIST=1 检测的轮廓不简历等级关系，检测所有轮廓
最常用：RETR_TREE=3，按照树形轮廓存储，从大到小，从右到左

method轮廓近似方法ApproximationMode
1、CHAIN_APPROX_NONE 保存所有轮廓上的点
2、CHAIN——APPROX——SIMPLE，只保存角点

返回contours和hierachy 返回轮廓和层级

绘制轮廓drawContours，非纯黑背景轮廓最外层序号为0

'''
import cv2
import numpy as np

img = cv2.imread(r'D:\xzc\python\opencv\diffshapes.jpeg')

#转变成单通道的黑白图片
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
cv2.imshow('img',img)
cv2.imshow('gray',img_gray)

#二值化
tresh, img_binary = cv2.threshold(img_gray, 200,255,cv2.THRESH_BINARY)

#查找轮廓，返回两个结果，分别是轮廓和层级
contours, hierarchy = cv2.findContours(img_binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(type(hierarchy))
print(hierarchy)
print(type(contours))
print(contours)
#绘制轮廓直接修改原图，想保持原图不变，建议copy一份
img_contours=cv2.drawContours(img,contours,-1,(0,0,255),2)  #-1表示绘制所有轮廓,可以通过编号选择想显示的轮廓，2表示线的粗细

#计算面积
area = cv2.contourArea(contours[1])
#计算周长
perimeter = cv2.arcLength(contours[1],closed=True)
print(area,perimeter)
cv2.imshow('source',img_contours)
cv2.imshow('gray',img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()