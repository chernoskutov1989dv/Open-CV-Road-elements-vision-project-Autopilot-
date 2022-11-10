import cv2
import numpy as np
cap = cv2.VideoCapture("D:/Progs/video2.mp4")

while True:
    success, img = cap.read()
    img = cv2.GaussianBlur(img, (9,9),0)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img= cv2.Canny(img, 100,100)
    kernel=np.ones((5,5), np.uint8)
    img= cv2.dilate(img, kernel, iterations=1)
    img= cv2.erode(img, kernel, iterations=1)


    cv2.imshow("Result", img)
    if cv2.waitKey(80) & 0xFF==ord("q"):
        break