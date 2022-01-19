import numpy as np
import cv2

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),5)
        roiGray = gray[y:y+w, x:x+w]
        roiColor = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5) #this one

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
