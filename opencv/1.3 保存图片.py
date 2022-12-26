# @Time: 2022/12/18 16:42
# @File: 1.3 保存图片.py
#使用imwrite(path,img)保存图片
import cv2
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.resizeWindow('img',640,480)
cat = cv2.imread(r'D:\xzc\python\opencv\cat.jpeg')
cv2.imshow('catimage',cat)
key = cv2.waitKey(0)
# if key & 0xFF == ord('q'):
#
cv2.imwrite(r'D:\xzc\python\opencv\luojicat.jpeg',cat)
cv2.destroyAllWindows()