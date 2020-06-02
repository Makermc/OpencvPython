#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@TIME  :2020/5/19 22:24
#@Author:Michael.ma
# Chapter-2
# 灰度,高斯模糊,边缘,扩张,侵蚀

import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5, 5), np.uint8)

# 灰度
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯模糊
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), sigmaX=0)
# 边缘
imgCanny = cv2.Canny(img, 150, 150)
# 扩张
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# 侵蚀
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)


cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Dilation', imgDilation)
cv2.imshow('Eroded', imgEroded)

cv2.waitKey(0)