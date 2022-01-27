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
        def drawBoundary(img,classifier,scaleFactor,minNeighbour,colour, text,clf):
            grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(grayImage,scaleFactor,minNeighbour)    

            coords = []
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(grayImage[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))

                # insert cursor
                conn = sqlite3.connect("programdatabase.db")
                c = conn.cursor()
                
                with conn:
                    c.execute("SELECT firstName from student WHERE studentID=" + str(id))
                    resultfName = c.fetchone()
                    resultfName = "+".join(resultfName)

                    c.execute("SELECT lastName from student WHERE studentID=" + str(id))
                    resultlName = c.fetchone()
                    resultlName = "+".join(resultlName)
                    
                if confidence > 77:
                    cv2.putText(img, f"{resultfName}", (x, y-55), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )
                    cv2.putText(img, f"{resultlName}", (x, y-30), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img, "Unknown face", (x, 5-55), FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3 )

                coords = [x,y,w,h]

            return coords
        def recognise(img,clf,faceCascade):
            coords = drawBoundary(img, faceCascade,1.1,10,(255,25,255),"Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognise(img, clf, faceCascade)
            cv2.imshow("Registration", img)

            if cv2.waitKey(1)==13:
                break
        videoCap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    main = Tk()
    app = Facerecognition(main)
    main.mainloop() 
