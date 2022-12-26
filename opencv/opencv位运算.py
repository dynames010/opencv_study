# @Time: 2022/12/25 20:04
# @File: opencv位运算.py
'''
python非运算 NOT
异或 不同为1 相同为0 ，异或符号  ^

opencv:
204 & 213  对应元素二进制与
非：
0 反过来 255 ~255， 相当于减去255
异或：
204^213
'''

cv2.bitwise_not()
cv2.bitwise_and()
cv2.bitwise_xor()

