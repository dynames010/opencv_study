# @Time: 2023/1/28 15:36
# @File: 5.5 形态学梯度.py
import cv2
import numpy as np
#定义核
kernel = np.ones((5,5), np.uint8)
img = cv2.imread(r'D:\xzc\python\opencv\jiaoyan2.jpg')

test_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
print(test_kernel)

#形态学梯度 = 原图-腐蚀
close_result = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,test_kernel,iterations=1)

#效果字体瘦一圈，去除长条形的噪声
cv2.imshow('img',close_result)
cv2.waitKey(0)
cv2.destroyAllWindows()