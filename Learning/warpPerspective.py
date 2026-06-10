import cv2 as cv
import numpy as np

img = cv.imread('Photos/Card.jpg')

width, height = 400, 210

pts1 = np.float32([
    [27,100],
    [403,54],
    [15,339],
    [509,252]
])

pts2 = np.float32([
    [0,0],
    [width,0],
    [0,height],
    [width,height]
])

matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

for x in range(4):
    cv.circle(img,
              (int(pts1[x][0]), int(pts1[x][1])),
              5,
              (0,255,0),
              cv.FILLED)

cv.imshow('Card', img)
cv.imshow('Output Image', imgOutput)
cv.waitKey(0)