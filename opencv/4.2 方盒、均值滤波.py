# @Time: 2023/1/2 21:37
# @File: 4.2 方盒、均值滤波.py
'''
方盒滤波
boxFilter(src,depth ksize,dst,anchor,normalize,bordertype)
normalize = True a=1/(W*H),一般情况均采用此种方式，此时 等同于均值滤波
normalize = False a=1
均值滤波
blur（src,ksize,dst,anchor,bordertype）
'''
import numpy as np
import cv2

lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
#只需要告诉方盒滤波，卷积核大小
dst = cv2.boxFilter(lihuacat, -1 ,(5,5),normalize=True)
cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()