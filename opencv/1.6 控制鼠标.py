# @Time: 2022/12/18 20:49
# @File: 1.6 控制鼠标.py
import cv2
import numpy as np

#函数随便去，参数必须是五个
#event表示鼠标事件（1,2,3,4……），可查看事件
#flag表示鼠标组合事件
def mouse_callback(event,x,y,flags,userdata):
    print(event,x,y,flags,userdata)
    if event == 2:
        cv2.destroyAllWindows()

#创建窗口
cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)
#宽度 高度
cv2.resizeWindow('mouse',640,360)

#设置鼠标的回调函数,setMouseCallback'123'即userdata
cv2.setMouseCallback('mouse',mouse_callback,'123')

#生成全黑图片
img = np.zeros((360,640,3), np.uint8)
while True:
    cv2.imshow('mouse',img)
    if cv2.waitKey(10) == ord('q'):
        break

cv2.destroyAllWindows()
