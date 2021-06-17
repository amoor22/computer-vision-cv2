from cv2 import cv2
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
img[256:] = 255, 0, 0
img[:256] = 255, 255, 255
cv2.line(img, (0, 0), (512, 512), (0))
cv2.rectangle(img, (200, 200), (400, 400), (0, 255, 0), cv2.FILLED)
cv2.circle(img, (256, 256), 20, (0, 0, 255), 5)
# cv2.imshow('image', img)
#  warp transform perspective
playing_img = cv2.imread("images/playing_cards.png")
width = 250
height = 350
pts1 = np.float32([[293, 96], [500, 155], [215, 387], [413, 440]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
warp = cv2.warpPerspective(playing_img, matrix, (width, height))
warpStack = np.hstack((warp, warp))
# cv2.imshow('warp', warp)
"""Color detection"""
def empty(a):
    pass
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar", 640, 240)
cv2.createTrackbar("hue min", 'trackbar', 0, 179, empty)
cv2.createTrackbar("hue max", 'trackbar', 179, 179, empty)
cv2.createTrackbar("sat min", 'trackbar', 31, 255, empty)
cv2.createTrackbar("sat max", 'trackbar', 255, 255, empty)
cv2.createTrackbar("val min", 'trackbar', 35, 255, empty)
cv2.createTrackbar("val max", 'trackbar', 255, 255, empty)
width = 640
height = 415
web_cam = cv2.VideoCapture(0)
web_cam.set(3, width)
web_cam.set(4, height)
web_cam.set(10, 150)
while True:
    success, lambo = web_cam.read()
    lamboHSV = cv2.cvtColor(lambo, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('hue min', 'trackbar')
    h_max = cv2.getTrackbarPos('hue max', 'trackbar')
    s_min = cv2.getTrackbarPos('sat min', 'trackbar')
    s_max = cv2.getTrackbarPos('sat max', 'trackbar')
    v_min = cv2.getTrackbarPos('val min', 'trackbar')
    v_max = cv2.getTrackbarPos('val max', 'trackbar')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(lamboHSV, lower, upper)
    result = cv2.bitwise_and(lambo, lambo, mask=mask)
    cv2.imshow('result', result)
    # cv2.imshow('lambo', lamboHSV)
    cv2.imshow('mask', mask)
    cv2.waitKey(1)
shapes = cv2.imread("images/shapes.png")
shapesCanny = cv2.Canny(shapes, 100, 100)
def getContour(img, target):
    #                                                                  gets all contours
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # negative one to draw the whole contour, we can use the area as a minimum threshold to avoid detecting noise
        if area > 100:
            cv2.drawContours(target, cnt, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            # approximates the number of corners in each contour
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCorner == 3: objName = "tri"
            elif objCorner == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.90 and aspRatio < 1.10:
                    objName = "square"
                else:
                    objName = "rect"
            elif objCorner > 7: objName = "circle"
            else: objName = "None"
            cv2.rectangle(target, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(target, objName, (x + (w // 2) - 15, y + (h // 2) - 15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0))
shapes_target = shapes.copy()
getContour(shapesCanny, shapes_target)
cv2.imshow("shapes", shapes_target)
cv2.waitKey(0)