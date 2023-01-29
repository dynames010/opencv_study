# @Time: 2023/1/28 15:48
# @File: 5.6 顶帽操作.py
#顶帽操作=原图-开运算，即 去除的噪点
#黑帽操作=原图-闭运算
import cv2
import numpy as np
#定义核
kernel = np.ones((5,5), np.uint8)
img = cv2.imread(r'D:\xzc\python\opencv\jiaoyan2.jpg')
open_result = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
test_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
print(test_kernel)
#顶帽
hat_result = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,test_kernel,iterations=1)
#黑帽
black_result = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,test_kernel,iterations=1)
#效果字体瘦一圈，去除长条形的噪声
cv2.imshow('img',np.hstack((open_result,hat_result)))
cv2.waitKey(0)
cv2.destroyAllWindows()
