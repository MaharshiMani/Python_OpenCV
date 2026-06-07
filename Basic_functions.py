import cv2 as cv
import numpy as np

frameWidth=640
frameHeight=420
kernel=np.ones((5,5),np.uint8)

path='Photos/Kratos.png'
img=cv.imread(path)

imgGray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgGray=cv.resize(imgGray,(frameWidth,frameHeight))
imgBlur=cv.GaussianBlur(imgGray,(7,7),0)
imgCanny=cv.Canny(imgBlur,100,250)
imgDilate=cv.dilate(imgCanny,kernel,iterations=1)
imgErode=cv.erode(imgDilate,kernel,iterations=1)

img=cv.resize(img,(frameWidth,frameHeight))

cv.imshow('Kratos',img)
cv.imshow('Gray Scale',imgGray)
cv.imshow('img Blur',imgBlur)
cv.imshow('img Canny',imgCanny)
cv.imshow('img Dialated',imgDilate)
cv.imshow('img Eroded',imgErode)
cv.waitKey(0)

