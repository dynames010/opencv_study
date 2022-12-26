# @Time: 2022/12/25 20:53
# @File: 2.8 resize.py
'''
缩放有四种插值算法，指定图片宽高
'''
import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
print(lihuacat.shape)
#邻近插值
new_cat1 = cv2.resize(lihuacat,dsize=(640,480),interpolation=cv2.INTER_NEAREST)
#双线性插值，使用原图中的4个点进行插值
new_cat2 = cv2.resize(lihuacat,dsize=(640,480),interpolation=cv2.INTER_LINEAR)
#三次插值，原图中的16个点
new_cat3 = cv2.resize(lihuacat,dsize=(640,480),interpolation=cv2.INTER_CUBIC)
#区域插值，效果最好，计算时间长
new_cat4 = cv2.resize(lihuacat,dsize=(640,480),interpolation=cv2.INTER_AREA)

#按照x轴y轴比例进行缩放
new_cat4 = cv2.resize(lihuacat,dsize=None, fx=0.5,fy=0.5)
cv2.imshow('img',np.hstack((new_cat1,new_cat2,new_cat3,new_cat4)))
cv2.waitKey(0)
cv2.destroyAllWindows()