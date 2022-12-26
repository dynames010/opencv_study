# @Time: 2022/12/22 14:06
# @File: 2.4图像通道的分离和合并.py
import cv2
import numpy as np
img = np.zeros((200,300,3),np.uint8)

#分割通道
b, g, r = cv2.split(img)
b[1:100] = 255
print(b)
img2 = cv2.merge((b,g,r))
cv2.imshow('img',np.hstack((img,img2)))
cv2.waitKey(0)
cv2.destroyAllWindows()