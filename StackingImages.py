import cv2 as cv
import numpy as np
import myUtilis

#path='Photos/Kratos.png'
#img=cv.imread(path)

#img=cv.imread('Photos/Landscape.jpg')
#cv.imshow('Landscape',img)
#cv.waitKey(0)

cap=cv.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

while True:
    success,img=cap.read()
    cv.imshow('Video',img)
    kernel=np.ones((5,5),np.uint8)

    imgGray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur=cv.GaussianBlur(img,(7,7),0)
    imgCanny=cv.Canny(imgBlur,100,250)
    imgDilate=cv.dilate(imgCanny,kernel,iterations=2)
    imgErode=cv.erode(imgDilate,kernel,iterations=1)


    #The below code is redundant, instead of that, we'll use a custom method defined in the myUtilis 


    # scale=0.5

    # img=cv.resize(img,(0,0),None,scale,scale)
    # imgGray=cv.resize(imgGray,(0,0),None,scale,scale)
    # imgBlur=cv.resize(imgBlur,(0,0),None,scale,scale)
    # imgCanny=cv.resize(imgCanny,(0,0),None,scale,scale)
    # imgDilate=cv.resize(imgDilate,(0,0),None,scale,scale)
    # imgErode=cv.resize(imgErode,(0,0),None,scale,scale)

    # imgGray=cv.cvtColor(imgGray,cv.COLOR_GRAY2BGR)
    # imgBlur=cv.cvtColor(imgBlur,cv.COLOR_GRAY2BGR)
    # imgCanny=cv.cvtColor(imgCanny,cv.COLOR_GRAY2BGR)
    # imgDilate=cv.cvtColor(imgDilate,cv.COLOR_GRAY2BGR)
    # imgErode=cv.cvtColor(imgErode,cv.COLOR_GRAY2BGR)

    # hor1=np.hstack((img,imgGray,imgBlur))
    # hor2=np.hstack((imgCanny,imgDilate,imgErode))
    # ver=np.vstack((hor1,hor2))

    # cv.imshow('Vertical',ver)


    ##Better Code using the custom function##


    StackedImages=myUtilis.stackImages(0.7,([img,imgGray,imgBlur],[imgCanny,imgDilate,imgErode]))
    # cv.imshow('Kratos',img)
    # cv.imshow('Gray Scale',imgGray)
    # cv.imshow('img Blur',imgBlur)
    # cv.imshow('img Canny',imgCanny)
    # cv.imshow('img Dialated',imgDilate)
    # cv.imshow('img Eroded',imgErode)
    cv.imshow('Stacked Images',StackedImages)
    if cv.waitKey(1) & 0xFF==ord('q'):
     break
