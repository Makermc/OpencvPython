#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@TIME  :2020/5/19 21:36
#@Author:Michael.ma
# Chapter-1
# 读取图片,读取视频,使用网络摄像头

import cv2
print("package improted")
# 读取照片
img = cv2.imread("Resources/lena.png")
cv2.imshow('Output', img)
cv2.waitKey(1000)

# 读取视频
cap = cv2.VideoCapture('Resources/SmartCar.mp4')
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 使用摄像头(默认摄像头为0)
cap = cv2.VideoCapture(0)
# 设置视频框长度
cap.set(3, 640)
# 设置视频框高度
cap.set(4, 480)
# 设置视频亮度
cap.set(10, 120)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


