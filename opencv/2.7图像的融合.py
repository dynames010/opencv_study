# @Time: 2022/12/25 19:58
# @File: 2.7图像的融合.py
import cv2
import numpy as np
lihuacat = cv2.imread(r'D:\xzc\python\opencv\lihuacat.jpeg')
luojicat = cv2.imread(r'D:\xzc\python\opencv\luojicat.jpeg')
new_lihuacat = lihuacat[0:320,0:320]
new_luojicat = luojicat[0:320,0:320]
#融合是按，图片一比重*图片一 + 图片二比例*图片二 + 偏执（调整图片明暗）
ronghe  = cv2.addWeighted(new_lihuacat,0.7,new_luojicat,0.3,10)
cv2.imshow('img',ronghe)
cv2.waitKey(0)
cv2.destroyAllWindows()