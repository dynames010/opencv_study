# @Time: 2023/1/2 16:13
# @File: 3.2 仿射变换之透视变换.py
'''
透视变换，把斜图变正
warpPerspective(img,M,dsize)
M是一个3*3的矩阵
getPerspectiveTransform(src,dst)取原图的四个点,生成变换矩阵
'''
import cv2
import numpy as np
guanggao = cv2.imread(r'D:\xzc\python\opencv\guanggaopai.jpeg')
src = np.float32([[96,33],[96,388],[413,156],[412,283]])
dst = np.float32([[0,0],[0,200],[400,0],[400,200]])
M = cv2.getPerspectiveTransform(src,dst)

#透视变换
new = cv2.warpPerspective(guanggao,M,(400,200))

cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',640,480)
cv2.imshow('img',new)

cv2.waitKey(0)
cv2.destroyAllWindows()