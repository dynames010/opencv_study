# @Time: 2023/1/29 20:43
# @File: 6.1 图像金字塔.py
'''
高斯金字塔：
向下采样：
抽取偶数行欧数列，向上图像变模糊,即下采样
向上采样：
1、将图像每个方向扩大为原来的两倍，偶数行列补0，
2、使用先前的内核与放大后图像卷积，获得近似值
API：
pyrDown()
pyrUp()

拉普拉斯金字塔：可用于图像压缩，利用拉普拉斯和高斯金字塔可以还原原图
由高斯金字塔经过多次向下采样和向上采样并且相减获取到的差值
'''
import cv2
import numpy as np

#读取图片
img = cv2.imread(r'D:\xzc\python\opencv\hand2.jpg')

print(img.shape)
#每次变小1/2
dst = cv2.pyrDown(img)
dst2 = cv2.pyrDown(dst)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

#向上采样
dst3 = cv2.pyrUp(img)
dst4 = cv2.pyrUp(dst3)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)

#拉普拉斯金字塔
dst5 = cv2.pyrUp(dst)
cv2.imshow('dst5',dst5)
#拉普拉斯金字塔即原图和高斯金字塔的差值，可以多次相减
lap0 = img - dst5
cv2.imshow('lap0',lap0)

cv2.waitKey(0)
cv2.destroyAllWindows()