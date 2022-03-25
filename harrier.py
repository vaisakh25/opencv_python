import cv2
import numpy as np

img = cv2.imread("Resources/harrier.jpg")

print(img.shape)

imgResize = cv2.resize(img, (640, 480))

print(imgResize.shape)

imgCropped = img[0:200, 0:150]

cv2.imshow("image", img)
cv2.imshow("image_resized", imgResize)
cv2.imshow("image_cropped", imgCropped)

cv2.waitKey(0)

