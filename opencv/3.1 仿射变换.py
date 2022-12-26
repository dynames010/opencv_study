# @Time: 2022/12/26 19:17
# @File: 3.1 仿射变换.py
'''
仿射变换是图像旋转、缩放、平移的总称
需要矩阵的知识，第一个矩阵的列数等于第二个矩阵的行数，主要计算变化矩阵M，最少是float 32位
cv2.warpAffine(src,M,dsize()，flag,mode,value)
flag:与resize插值算法一致
mode：边界外推法标志
value:填充边界值
https://www.bilibili.com/video/BV12Z4y1z7jb/?p=28&spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=618b25933e79081c1aa9f94044ef08f2
(x,y)=(x+tx,y+ty)  x轴平移tx，y轴平移ty，可以理解为y轴箭头朝下？
'''

import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
h,w,ch = lihuacat.shape
M = np.float32([[1,0,200],[0,1,60]])
#opencv先宽度，再高度
new_cat2 = cv2.warpAffine(lihuacat,M,dsize=(w,h))
cv2.imshow('cat',new_cat2)
cv2.waitKey(0)
cv2.destroyAllWindows()