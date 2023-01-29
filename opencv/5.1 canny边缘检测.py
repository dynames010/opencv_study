# @Time: 2023/1/27 20:30
# @File: 5.1 canny边缘检测.py
import cv2
import numpy as np

lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
cat1 = cv2.Canny(lihuacat,100,500)  #数字分别对应 最大最小阈值，可以给小一点阈值，得到较为精细的边缘
cat2 = cv2.Canny(lihuacat,80,120)
cv2.imshow('lihuacat',np.hstack((cat1,cat2)))
cv2.waitKey()
cv2.destroyAllWindows()