import numpy as np
import cv2
from pyzbar.pyzbar import decode

# img = cv2.imread('resources/img.png')
# code = decode(img)
cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 640)

while True:

    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 255), 2)
        # print(barcode.rect)
        print()
    # print(code)
    cv2.imshow('Result', img)
    cv2.waitKey(1)

