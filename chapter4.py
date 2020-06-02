#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@TIME  :2020/5/19 22:38
#@Author:Michael.ma
# Chatper-4
# 在图片上绘制东西,放置文本

import cv2
import numpy as np
# 0为黑色
img = np.zeros((512, 512, 3), np.uint8)
# # 第一个参数为高度,第二个参数为宽度
# img[200:300, 100:300] = 255, 0, 0

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255))
# 图片, 起点, 对角点, 颜色, 粗细, 填充
cv2.rectangle(img, (0, 0), (250, 300), (0, 255, 0), 5, cv2.FILLED)
# 图片, 圆心, 半径, 颜色, 粗细
cv2.circle(img, (256, 256), 50, (0, 255, 255), 10)
# 图片, 内容, 起点, 字体, 大小, 颜色, 粗细
cv2.putText(img, 'OpenCV', (350, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 180, 0), 2)


cv2.imshow('Image', img)
cv2.waitKey(0)