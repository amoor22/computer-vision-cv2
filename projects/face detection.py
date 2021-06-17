from cv2 import cv2
from time import sleep
face_cascade = cv2.CascadeClassifier(r"C:\Users\abdul\PycharmProjects\Web-Scraping\cv2\tutorial\haar cascade.xml")
web_cam = cv2.VideoCapture(0)
web_cam.set(3, 500)
web_cam.set(4, 700)
web_cam.set(10, 100)
while True:
    # img = cv2.imread("images/face.jpg")
    success, img = web_cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv2.imshow("result", img)
    cv2.waitKey(1)
    sleep(0.05)