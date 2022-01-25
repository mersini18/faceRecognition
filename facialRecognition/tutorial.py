import numpy as np
import cv2

# initialise the webcam 
cap = cv2.VideoCapture(0)

# import face and eye classifiers
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# infinite loop to keep camera feed running
while True:
    # create variable frame to store the video output
    ret, frame = cap.read()

    # gray variable changes the video output to greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # machine learning used to detect faces found in greyscale image
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    # takes co-ordinates of outline of the 3D face image
    for (x,y,w,h) in faces:
        # creates a rectangle around detected face using rgb colour scheme
        cv2.rectangle(frame, (x,y), (x+w+1, y+h+5), (255,0,0),5)
        # defines an area of interest which is the co-ordinates of where a face is detected
        roiGray = gray[y:y+w, x:x+w]
        roiColor = frame[y:y+h, x:x+w]
        # machine learning used to detect eyes found in greyscale image of the area of interest (face)
        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)
        # co-ordinates of detected eyes
        for (ex, ey, ew, eh) in eyes:
            # creates a rectangle around the eyes, in a different colour to the rectagle around face
            cv2.rectangle(roiColor, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)

    # displays the frame on the screen so user can see
    cv2.imshow('Frame', frame)
    # video will run infintely until 'q' is pressed 
    if cv2.waitKey(1)== ord('q'):
        break
# releases the camera from the program so it can be used on other applications
cap.release()
# destroys the frame window
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
