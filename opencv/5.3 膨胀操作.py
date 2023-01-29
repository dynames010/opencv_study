# @Time: 2023/1/28 10:54
# @File: 5.3 膨胀操作.py
#膨胀是腐蚀的反操作
import cv2
import numpy as np
#定义核

img = cv2.imread(r'D:\xzc\python\opencv\math.jpeg')

#获取形态学卷积核
#椭圆cv2.MORPH_ELLIPSE为生成卷积核的形状cv2.MORPH_RECT、十字架cv2.MORPH_CROSS
test_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(test_kernel)

img_result = cv2.dilate(img,test_kernel,iterations=2)
#效果字体胖一圈
cv2.imshow('img',img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()