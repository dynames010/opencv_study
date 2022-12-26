# @Time: 2022/12/22 15:47
# @File: homework mousedraw.py
'''
按下按键不如l,进入绘制直线模式，需要记录起始位置，即按下鼠标左键的一瞬间的坐标位置，左键起来的鼠标坐标作为终点，然后绘制
'''

import cv2
import numpy as np
start_plot = (0,0)
end_plot = (0,0)
curshape = 0
img = np.zeros((480,680,3),np.uint8)

def mouse_callback(event,x,y,flags,userdata):
    global curshape,start_plot,end_plot
    if event == cv2.EVENT_LBUTTONDOWN:
        start_plot = (x,y)
    if event == cv2.EVENT_LBUTTONUP:
        end_plot = (x,y)
        if curshape == 0:
            cv2.line(img,start_plot,end_plot,(0,0,255),5,16)
        if curshape == 1:
            a = start_plot[0] - end_plot[0]
            b = start_plot[1] - end_plot[1]
            length = int((a**2 + b**2)**0.5)
            cv2.circle(img,start_plot,length,(0,250,0),6,16)
        if curshape == 2:
            cv2.rectangle(img, start_plot, end_plot, (0, 255, 0), 5, 16)

cv2.namedWindow('mouse',cv2.WINDOW_NORMAL)
cv2.resizeWindow('mouse',640,480)
cv2.setMouseCallback('mouse', mouse_callback, '123')

while True:
    cv2.imshow('mouse', img)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('l'):
        curshape = 0
    elif key == ord('c'):
        curshape = 1
    elif key == ord('r'):
        curshape = 2

cv2.destroyAllWindows()


cv2.waitKey(0)