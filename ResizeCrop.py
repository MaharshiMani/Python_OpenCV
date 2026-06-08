import cv2 as cv

path='Photos/Kratos.png'
img=cv.imread(path)
print(img.shape)

width,height=1024,768
imgResize=cv.resize(img,(width,height))
print(imgResize.shape)

imgCropped=imgResize[270:1024,130:470]
imgCroppedResize=cv.resize(imgCropped,(imgResize.shape[1],imgResize.shape[0]))

cv.imshow('Kratos',img)
cv.imshow('resized_kratos',imgResize)
cv.imshow('Cropped Kratos',imgCropped)
cv.imshow('Resized Cropped Image',imgCroppedResize)
cv.waitKey(0)