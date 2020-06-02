#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@TIME  :2020/5/19 22:25
#@Author:Michael.ma
# Chapter-3
# 调整图片形状 裁剪

import cv2
import numpy as np

img = cv2.imread('Resources/lena.png')
print(img.shape)
# 调整大小  (宽,高)
imgResize = cv2.resize(img, (250, 400))
# 打印形状时显示方式为(高,宽,通道数)
print(imgResize.shape)
# 裁剪[高度范围,宽度范围]
imgCropped = img[0:200, 200:500]

cv2.imshow('Image', img)
cv2.imshow('ImageResize', imgResize)
cv2.imshow('ImgCropped', imgCropped)

cv2.waitKey(0)