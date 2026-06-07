import cv2 as cv
#img=cv.imread('Photos/Landscape.jpg')
#cv.imshow('Landscape',img)
#cv.waitKey(0)

frameWidth=500
frameHeight=500

cap=cv.VideoCapture('Videos/Drone.mp4')
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

while True:
    success,img=cap.read()
    img=cv.resize(img,(frameWidth,frameHeight))
    cv.imshow('Video',img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break