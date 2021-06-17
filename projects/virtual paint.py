from cv2 import cv2
import numpy as np
width = 640
height = 415
web_cam = cv2.VideoCapture(0)
web_cam.set(3, width)
web_cam.set(4, height)
web_cam.set(10, 150)
colors = [
    [100, 72, 255, 179, 255, 255],
    [70, 255, 101, 179, 255, 255],
    [161, 72, 35, 179, 255, 255]

]
color_val = [[255, 0, 0],
             [0, 255, 0],
             [0, 0, 255]
]
def getContour(img, target):
    #                                                                  gets all contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # negative one to draw the whole contour, we can use the area as a minimum threshold to avoid detecting noise
        if area > 100:
            # cv2.drawContours(target, cnt, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # approximates the number of corners in each contour
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
    return x + (w // 2), y
circles = []
def findColor(img, colors, color_val):
    for i, color in enumerate(colors):
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # result = cv2.bitwise_and(img, img, mask=mask)
        x, y = getContour(mask, imgC)
        if (x, y) != (0, 0):
            circles.append((x, y, color_val[i])) 
        # cv2.circle(img, (x, y), 15, color_val[i], cv2.FILLED)
        # cv2.imshow(str(color[0]),result)
    for c in circles:
        x, y, col = c
        cv2.circle(img, (x, y), 10, col, cv2.FILLED)
while True:
    success, img = web_cam.read()
    imgC = img.copy()
    # cv2.imshow("web cam", img)
    findColor(img,colors, color_val)
    cv2.imshow('result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break