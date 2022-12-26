# @Time: 2022/12/26 17:06
# @File: 2.9 图像的反转旋转.py
'''
图像的翻转
flip(src,flipCode)
flipCode = 0 表示上下翻转
flipCode > 0 表示左右翻转
flipCode < 0 上下+左右

图像的旋转
rotate(src,rotateCode = ROTATE_)
ROTATE_90_CLOCKWISE  90度顺时针
ROTATE_180 180度
ROTATE_90_COUNTERCLOCKWISE  90度逆时针
'''

import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
new_cat = cv2.flip(lihuacat, 0)
new_cat1 = cv2.flip(lihuacat, 1)
new_cat2 = cv2.flip(lihuacat, -1)
new_cat3 = cv2.rotate(lihuacat, rotateCode = cv2.ROTATE_90_CLOCKWISE)
#new_cat2 = lihuacat[::-1, ::-1]

cv2.imshow('cat_rotate',new_cat3)
cv2.imshow('cat',np.hstack((lihuacat,new_cat2)))
cv2.waitKey(0)
cv2.destroyAllWindows()


