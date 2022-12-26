# @Time: 2022/12/22 15:20
# @File: 2.5 显示文字.py
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
img = cv2.imread(r'D:\xzc\python\opencv\cat.jpeg')
#纯白
#img = np.full((200,200,3),fill_value=255 ,dtype=np.uint8)
#导入字体文件
font = ImageFont.truetype('./msyh.ttc',15)

#创建一个pillow图片
img_pill = Image.fromarray(img)

draw = ImageDraw.Draw(img_pill)

#用draw绘制中文
draw.text((10,150),'你好',font=font,fill=(0,255,0,0))

#重新变回ndarray
img = np.array(img_pill)
cv2.imshow('img',img)
cv2.waitKey(0)