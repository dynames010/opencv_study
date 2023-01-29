# @Time: 2023/1/28 11:02
# @File: 5.4 开闭运算.py
#开运算=腐蚀+膨胀，提供另一种去除噪声思路,可以消除图形外的椒盐噪声
#闭运算=膨胀+腐蚀,可以去除图形内部的噪声
import cv2
import numpy as np
#定义核
kernel = np.ones((5,5), np.uint8)
img = cv2.imread(r'D:\xzc\python\opencv\jiaoyan2.jpg')

test_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
print(test_kernel)
#腐蚀+膨胀
img_change = cv2.erode(img,test_kernel,iterations=2)
img_result = cv2.dilate(img_change,test_kernel,iterations=2)

#也可以直接调用api实现开运算
open_result = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
close_result = cv2.morphologyEx(img,cv2.MORPH_CLOSE,test_kernel,iterations=2)
#效果字体瘦一圈，去除长条形的噪声
cv2.imshow('img',close_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
