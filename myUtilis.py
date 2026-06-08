import cv2
import numpy as np

#Method to stack multiple images

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])

    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    for y in range(rows):
        for x in range(cols):
            img = imgArray[y][x]

            # Resize image to match first image's dimensions
            if img.shape[:2] != (height, width):
                imgArray[y][x] = cv2.resize(img, (width, height))

            # Convert grayscale to BGR
            if len(imgArray[y][x].shape) == 2:
                imgArray[y][x] = cv2.cvtColor(
                    imgArray[y][x],
                    cv2.COLOR_GRAY2BGR
                )

            # Apply scaling
            imgArray[y][x] = cv2.resize(
                imgArray[y][x],
                (0, 0),
                fx=scale,
                fy=scale
            )

    # Stack images row-wise
    hor = [np.hstack(row) for row in imgArray]

    # Stack rows vertically
    ver = np.vstack(hor)

    return ver