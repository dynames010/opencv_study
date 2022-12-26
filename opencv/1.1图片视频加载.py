import cv2
#WINDOW_AUTOSIZE不允许修改窗口大小
cv2.namedWindow('window',cv2.WINDOW_NORMAL)
#python函数编码规范，单词首字母小写，单词单词之间下划线连接
#改变窗口的大小
#cv2.resizeWindow('window',800,600)
#展示名字为window的窗口
cv2.imshow('new',0)
#watikey返回按键的ascii的值
#0接受任意按键，给其他参数，表示等待时间，单位毫秒,,销毁窗口
key = cv2.waitKey(0)    #返回int型号
if key & 0xFF == ord('q'):  #ascii是八位，int是十六位 均变成16位后进行比较
    print('准备销毁窗口')
    cv2.destroyAllWindows()


#计算q的ascii码
print(ord('q')) #计算ascii码函数
print(type(ord('q')))
