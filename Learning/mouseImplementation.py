import cv2 as cv
import numpy as np

circle=np.zeros((4,2),np.int32)
counter=0

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv.EVENT_LBUTTONDOWN:
        circle[counter]=x,y
        counter = counter+1
        print(circle)

img=cv.imread('Photos/Book.jpg')
width,height=512,360
img=cv.resize(img,(width,height))
while True:

    if counter ==4:

        pts1 = np.float32([
            circle[0],
            circle[1],
            circle[2],
            circle[3]
        ])

        pts2 = np.float32([
            [0,0],
            [width,0],
            [0,height],
            [width,height]
        ])

        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv.warpPerspective(img, matrix, (width,height))
        cv.imshow('Output Image', imgOutput)
    for x in range(4):
        cv.circle(img,
                (int(circle[x][0]), int(circle[x][1])),
                2,
                (0,255,0),
                cv.FILLED)
    cv.imshow('Book', img)
    cv.setMouseCallback('Book', mousePoints)
    cv.waitKey(1)
    
