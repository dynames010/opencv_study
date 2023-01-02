# @Time: 2023/1/2 15:33
# @File: 4.1 卷积操作.py
'''
filter2D(src,ddeth,kernel,dst,anchor,delta,bordertype)
depth是卷积后图片的位深，一般设为-1，和原图一致
kernel是卷积核大小，用元组或ndarray表示，类型必须是float幸
anchor锚点，卷积核中心，默认-1-1
delta可选参数
'''
import numpy as np
import cv2

lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')

#原始图片汇总每个点被平均，图像边模糊,kernel必须是float型
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(lihuacat, -1, kernel)

#尝试不同卷积核
kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

