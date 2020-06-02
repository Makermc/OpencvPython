import cv2
import numpy as np

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
        # if area > 500:
        cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt,True)
        # print(peri)
        approx = cv2.approxPolyDP(cnt,0.02*peri,True)
        # print(len(approx))
        objCor = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        if objCor == 3:
            ObjectType = 'Triangle'
        elif objCor == 4:
            aspRatio = w/float(h)
            if aspRatio>0.9 and aspRatio<1.1:
                ObjectType='Squre'
            else:
                ObjectType='Rectangle'
        elif objCor > 4:
            ObjectType='Circle'
        else:
            ObjectType = 'None'
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(imgContour,ObjectType,
                    (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)





path = 'Resources/shapes.jpg'

img  = cv2.imread(path)
imgContour = img.copy()

imgGray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)

# cv2.imshow('Original', img)
# cv2.imshow('ImageGray', imgGray)
# cv2.imshow('ImageBlur', imgBlur)
# cv2.imshow('ImageCanny', imgCanny)
# cv2.imshow('ImageBlank', imgBlank)
cv2.imshow('ImageContours', imgContour)



cv2.waitKey(0)