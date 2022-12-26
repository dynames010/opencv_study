# @Time: 2022/12/22 13:43
# @File: 深浅拷贝.py
import cv2
import numpy as np
img = cv2.imread(r'D:\xzc\python\opencv\cat.jpeg')
img1 = img.view()
img2 = img.copy()
print(img[10,10])
img[10:100,10:100] = [0,0,255]

print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('show', np.hstack((img,img1,img2)))
cv2.waitKey(0)
cv2.destryAllWindows()

