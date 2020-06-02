import cv2
import numpy as np

print('Package Imported')
# 图像局部变换
img = cv2.imread('Resources/card.jpg')
# 设置输出参数
width,height = 250,350
# 原图中需要转换的图的坐标position，可有画图原件获得
pts1 = np.float32([[275,22],[498,171],[42,386],[275,527]])
# 输出图片参数，矩形四个点
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# 获取变换矩阵
matrix = cv2.getPerspectiveTransform(pts1,pts2)
# 传参：原图，变换矩阵，显示区域
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow('card', img)
cv2.imshow('output', imgOutput)

cv2.waitKey(0)

# left-top(275,22) right-top(498,171) left-bottom(42,386) right-bottom(275,527)