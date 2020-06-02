import cv2
import numpy as np 

img = cv2.imread('Resources/lena.png')

imgHorizon = np.hstack((img,img))
imgVertical = np.vstack((img,img))

cv2.imshow("imgHorizon",imgHorizon)
cv2.imshow("imgVertical",imgVertical)




cv2.waitKey(0)