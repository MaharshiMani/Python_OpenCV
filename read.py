import cv2 as cv
#img=cv.imread('Photos/Landscape.jpg')
#cv.imshow('Landscape',img)
#cv.waitKey(0)

frameWidth=1024
frameHeight=768

cap=cv.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

while True:
    success,img=cap.read()
    cv.imshow('Video',img)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break