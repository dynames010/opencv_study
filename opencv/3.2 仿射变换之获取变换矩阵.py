# @Time: 2022/12/26 20:01
# @File: 3.2 仿射变换之获取变换矩阵.py
'''
getRotationMatrix2D(center,angle,scale)
angle 规定为逆时针
get AffineTransform(src[],dst[])通过三点确定变换后位置，解出三个点对应方程，获取偏移参数和旋转角度
'''
import numpy as np
import cv2

lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')

M = cv2.getRotationMatrix2D([100,100],15,1.5)

print(M)
cat = cv2.warpAffine(lihuacat,M,(1920,1080))

src = np.float32([[10,20],[100,200],[60,70]])
dst = np.float32([[30,30],[150,150],[70,80]])

M2 = cv2.getAffineTransform(src,dst)

cat2 = cv2.warpAffine(lihuacat,M2,(1920,1080))

cv2.imshow('img',cat2)

cv2.waitKey(0)
cv2.destroyAllWindows()