from cv2 import cv2
import numpy as np

web_cam = cv2.VideoCapture(0)
# 3 : width, 4 : height, 10 : brightness
web_cam.set(3, 640)
web_cam.set(4, 310)
web_cam.set(10, 100)

kernel = np.ones((5, 5), np.uint8)

while True:
    break
    success, img = web_cam.read()
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    # the higher the threshold value the less edges it detects
    # dilation makes edges bigger while erosion makes edges smaller
    # the bigger the numpy array for the kernel the more it moves to the right and down
    imgCanny = cv2.Canny(img, 100, 100)
    imgDilated = cv2.dilate(imgCanny, kernel, iterations=1)
    cv2.imshow("video", imgCanny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
img = cv2.imread(r"images/lambo.png")
# img = img[100:300, 30:img.shape[1] - 30]
imCanny = cv2.Canny(img, 100, 100)
imDilated = cv2.dilate(imCanny, kernel, iterations=1)
imEroded = cv2.erode(imDilated, kernel, iterations=1)
#                           (width, height)
imResized = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
#              [height, width]
imCropped = img[30:, 30: img.shape[1] - 30]
cv2.imshow('canny', imCanny)
cv2.imshow('eroded', imEroded)
cv2.imshow("dilated", imDilated)
# cv2.imshow("resized", imCropped)
cv2.waitKey(0)
