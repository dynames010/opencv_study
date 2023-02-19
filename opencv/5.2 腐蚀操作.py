# @Time: 2023/1/28 10:41
# @File: 5.2 腐蚀操作.py
#通过卷积核扫描图像，卷积核一般是1，图片中有一点黑色，卷积核出来就会有黑色，多次扫描，腐蚀效果更明显
#腐蚀通过卷积核，把矩阵中心位置取最小值；膨胀取最大值；例3*3的全1核矩阵，腐蚀后，中心位置取九宫格的最小值
#腐蚀erode支持参数erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
import cv2
import numpy as np
#定义核
kernel = np.ones((5,5), np.uint8)
img = cv2.imread(r'D:\xzc\python\opencv\math.jpeg')

#获取形态学卷积核
#椭圆cv2.MORPH_ELLIPSE为生成卷积核的形状cv2.MORPH_RECT、十字架cv2.MORPH_CROSS
test_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(test_kernel)

img_change = cv2.erode(img,kernel,iterations=1)
#效果字体瘦一圈，去除长条形的噪声
cv2.imshow('img',img_change)
cv2.waitKey(0)
cv2.destroyAllWindows()
