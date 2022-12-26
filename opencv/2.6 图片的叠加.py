# @Time: 2022/12/25 18:02
# @File: 2.6 图片的叠加.py
import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
luojicat = cv2.imread(r'D:\xzc\python\opencv\luojicat.jpeg')
new_lihuacat = lihuacat[0:320,0:320]
new_luojicat = luojicat[0:320,0:320]
print(new_lihuacat.shape)
print(new_luojicat.shape)

#cv加法操作，要求两个图片长宽相同，通道数相同，加法规则，两个图对应位置的元素相加，超过255均变成255
result = cv2.add(new_luojicat,new_lihuacat)

#和单个数字运算规则，超出255，会被截断，相当于%255
test = lihuacat + 100

#cv减法操作,减完小于零均变为0
cv2.subtract(new_luojicat,new_lihuacat)

#cv乘法操作multiply
cv2.multiply(new_luojicat,new_lihuacat)

cv2.divide(new_luojicat,new_lihuacat)

cv2.imshow('img',test)
cv2.waitKey(0)
cv2.destroyAllWindows()