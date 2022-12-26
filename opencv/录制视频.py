# @Time: 2022/12/18 20:35
# @File: 录制视频.py
import cv2
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 1920, 1080)

cap = cv2.VideoCapture(r'D:\xzc\Overwatch 2022.05.11 - 19.10.41.03.DVR.mp4')

#vm = cv2.VideoWriter_fourcc(*'mp4V')
#选择视频格式 avi格式
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
vm = cv2.VideoWriter('output.mp4',fourcc,30,(1920,1080))

while cap.isOpened():
    ret ,frame = cap.read()
    if not ret:
        break
    vm.write(frame)
    cv2.imshow('video',frame)

    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
vm.release()
cv2.destroyAllWindows()
