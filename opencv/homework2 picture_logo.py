# @Time: 2022/12/26 14:53
# @File: homework2 picture_logo.py
'''
作业目标：
1、引入图片
2、设计logo
3、规划logo的预期位置
4、add方法叠加
'''
import cv2
import numpy as np

lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')

#创建logo
logo = np.zeros((200,200,3),np.uint8)
logo[20:120,20:120] = (0,0,255)
logo[80:180,80:180] = (0,255,0)

#掩码，与运算结果后，为True，返回，为False,与mask掩码做与运算，与结果是True，返回原图像素，否则返回0
mask = np.zeros((200,200),np.uint8)
#掩码部分为黑色
mask[20:120,20:120] = 255
mask[80:180,80:180] = 255
m = cv2.bitwise_not(mask)
cv2.imshow('m',m)
cv2.waitKey(0)
test = cv2.bitwise_and(lihuacat, lihuacat, mask=m)
dst = cv2.add(test, logo)
lihuacat[:200,:200] = dst
cv2.imshow('test',test)
cv2.imshow('logo',logo)
cv2.imshow('img',lihuacat)
cv2.waitKey(0)
cv2.destroyAllWindows()
