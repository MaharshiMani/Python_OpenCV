import cv2 as cv
import numpy as np

img=np.zeros((512,512,3),np.uint8)
#img[:]=0,0,255

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)
cv.rectangle(img,(350,100),(450,300),(0,0,255),cv.FILLED)
cv.circle(img,(150,450),50,(255,0,0),3)
cv.putText(img,"Noice Boii",(75,50),cv.FONT_HERSHEY_COMPLEX,1,(0,123,0),1)

cv.imshow('Blank',img)
cv.waitKey(0)