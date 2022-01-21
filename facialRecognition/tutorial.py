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

# # cv2.data.haarcascades + 
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")                
                
# def faceCropped(frame):
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(gray, 1.3, 5)
#       # scaling factor = 1.3
#     #  minimum neighbor = 5
#     for (x,y,w,h) in faces:
#         faceCropped=frame[y:y+h, x:x+w]            
#         return faceCropped
        
# cap = cv2.VideoCapture(0)
# imgID = 0                
# while True:
#     ret, frame = cap.read()                        
#     if faceCropped(frame) is not None:
#         imgID +=1
                    
#     face = cv2.resize(faceCropped(frame), (450,450))
#     face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#     filenamePath = "data/user."+str(id)+"."+str(imgID)+".jpg"        
#     cv2.imwrite(filenamePath, face)
#     cv2.putText(face,str(imgID),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#     cv2.imshow("Cropped Face", face)

#     if cv2.waitKey(1) == 13 or int(imgID)==100:
#         break
                    
#     cap.release()
#     cv2.destroyAllWindows()
