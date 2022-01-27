from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import sqlite3
import cv2
import numpy as np
import os

class Train:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        self.trainButton = Button(self.main, text='Train data set', command=self.trainClassifier, width=20, height=3) 
        self.trainButton.pack()
 
    # Face classifier function

    def trainClassifier(self):
        # Directory of where images are stores (raw string)
        dataDirectory = (r"/Users/benjamin/Documents/GitHub/project/facialRecognition/data")
        # path is set to the image for each of the files within the data directory
        path= [os.path.join(dataDirectory,file) for file in os.listdir(dataDirectory)]

        # empty lists faces, ids
        faces=[]
        ids=[]

        # for loop to iterate through each image in directory to train classifier
        for image in path:
            # converts image to gray scale
            img=Image.open(image).convert('L') #Grayscale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            # displays faces to screen
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)


        # Train classifier

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed")
         



if __name__ == '__main__':
    main = Tk()
    app = Train(main)
    main.mainloop() 
