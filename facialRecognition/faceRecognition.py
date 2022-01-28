from this import s
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import cv2
from cv2 import FONT_HERSHEY_COMPLEX
from cv2 import VideoCapture
import numpy as np
import os

class Facerecognition:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Recognition System')

        self.titlelabel = Label(self.main, text = 'Registration screen', width=100, height =3, font = ('Arial', 20), bg = 'lightblue')
        self.titlelabel.grid(row=0,column=0,columnspan=7)

        self.startRegister = Button(self.main, text='Start register',  command = self.register,width=20, height=3) 
        self.startRegister.grid(row=1,column=0)


    # Face recognition - register

    def register(self):
        # this function will be used to draw a rectangle around a detected face when
        # registration is taken from the program
        def drawBoundary(img,classifier,scaleFactor,minNeighbour,colour, text,clf):
            # converts image to grayscale which is the format used for face detection
            grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # detects objects of different sizes in the input image
            # the detected objects are returned as a list of rectangles.
            features = classifier.detectMultiScale(grayImage,scaleFactor,minNeighbour)    

            coords = []

            for (x,y,w,h) in features:
                # draw rectangle around detected face
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                # prediction of a given sample image, that means a face
                id,predict = clf.predict(grayImage[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))

                # connect to database
                conn = sqlite3.connect("programdatabase.db")
                c = conn.cursor()
                
                with conn:
                    # get student first name from table which matches id of face found
                    c.execute("SELECT firstName from student WHERE studentID=" + str(id))
                    resultfName = c.fetchone()
                    resultfName = "+".join(resultfName)

                     # get student last name from table which matches id of face found
                    c.execute("SELECT lastName from student WHERE studentID=" + str(id))
                    resultlName = c.fetchone()
                    resultlName = "+".join(resultlName)

                # if a program predics a face has been found that matches dataset
                # will draw a rectangle around face and name it 
                if confidence > 77:
                    cv2.putText(img, f"{resultfName}", (x, y-55), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )
                    cv2.putText(img, f"{resultlName}", (x, y-30), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown face", (x, 5-55), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )

                coords = [x,y,w,h]
                return coords

        # Function to detect a face
        def recognise(img,clf,faceCascade):

            coords = drawBoundary(img, faceCascade,1.1,10,(255,25,255),"Face", clf)
            return img

        # initialises a face classifier through the haarcascade funtion
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        # reads the classifier.xml file I created earlier
        clf.read("Classifier.xml")
        
        # captures video footage from camera
        videoCap = cv2.VideoCapture(0)

        # infinite loop
        while True:
            ret, img = videoCap.read()
            # passes image through recognise funciton with classifier and cascade
            img = recognise(img, clf, faceCascade)
            # displays window to user with title
            cv2.imshow("Registration", img)

            # if enter key is pressed
            if cv2.waitKey(1)==13:
                break
        videoCap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    main = Tk()
    app = Facerecognition(main)
    main.mainloop() 
