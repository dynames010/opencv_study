# @Time: 2023/1/27 20:46
# @File: 5.1 自适应二值化.py
import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\math.jpeg')

#二值化对灰度图操作，把dog变为灰度图
gray = cv2.cvtColor(lihuacat,cv2.COLOR_BGR2GRAY)
#threshold返回两个值，一个是阈值，一个是处理后的图片
#参数:灰度图，阈值，最大值，type方式
thresh,img = cv2.threshold(gray,110,255,cv2.THRESH_BINARY)
print(thresh)

#自适应阈值二值化
#3为邻域大小，值越大，画面越不精细，adaptive为阈值计算方法取相邻区域的加权和；0为常数，阈值等于平均值减去这个常数
dst = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,3,0)
media = cv2.medianBlur(dst,5)

cv2.imshow('lihuacat',media)
cv2.waitKey()
cv2.destroyAllWindows()