# # @Time: 2022/12/18 16:04
# # @File: 加载显示图片.py
import cv2
import matplotlib as plt
cat = cv2.imread(r'D:\xzc\python\opencv\cat.jpeg')
print(cat)
#plt.imshow(cat)
#通过matplotlib方法预览效果和cv预览效果不同，原因，opencv读取图片不是RGB事BGR，用其余方式展示就会出现问题
#plt.show(cat)

cv2.imshow('cat',cat)
cv2.waitKey(0)
cv2.destroyAllWindows()

#展示图片代码封装程函数，方便重用,从外部文件导入工具类：
def cv_show(name , img):
    cv2.imshow(name ,img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()

#封装到util中
# from util import cv_show
# cat = cv2.imread(r'D:\xzc\python\opencv\cat.jpeg')
# cv_show('cat',cat)