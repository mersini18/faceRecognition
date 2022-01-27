
from tkinter import *
from tkinter import ttk
from student import Student
from train import Train
from faceRecognition import Facerecognition
import os

class Face_Recognition_System:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        self.titlelabel = Label(self.main, text = 'Facial Recognition Attendance System', width=100, height =3, font = ('Arial', 20), bg = 'lightblue')
        self.titlelabel.grid(row=0,column=0,columnspan=7)

        self.blank = Label(self.main, text = '', height = 2)
        self.blank.grid(row=1)

        self.addStudentbutton = Button(self.main, text = 'Student details', command = self.studentDetails, width=20, height=3)
        self.addStudentbutton.grid(row =2,column =2, columnspan=1)
        self.viewClassbutton = Button(self.main, text = 'View Class', width=20, height=3)
        self.viewClassbutton.grid(row =2,column =3, columnspan=1)
        self.attendancebutton = Button(self.main, text = 'Start registration', command= self.startRegister, width=20, height=3)
        self.attendancebutton.grid(row =2,column =4, columnspan=1)

        self.blank = Label(self.main, text = '', height = 2)
        self.blank.grid(row=3)

        self.trainDatabutton = Button(self.main, text = 'Train Data', command=self.trainData, width=20, height=3)
        self.trainDatabutton.grid(row = 4,column =2, columnspan=1)
        self.openPhotos = Button(self.main, text = 'Photos', command = self.openImage, width=20, height=3)
        self.openPhotos.grid(row =4,column =3, columnspan=1)
        self.quitbutton = Button(self.main, text = 'Quit', command =self.quit, width=20, height=3)
        self.quitbutton.grid(row =4,column =4, columnspan=1)

    def openImage(self):
        os.startfile(r'C:\Users\benja\OneDrive\Documents\GitHub\project\facialRecognition\data')
    # Functions buttons

    # Student details button
    def studentDetails(self):
        self.newWindow = Toplevel(self.main)
        self.app = Student(self.newWindow)

    # Train data button
    def trainData(self):
        self.newWindow = Toplevel(self.main)
        self.app = Train(self.newWindow)

    # Registration button
    def startRegister(self):
        self.newWindow = Toplevel(self.main)
        self.app = Facerecognition(self.newWindow)    

    def quit(self):
        self.main.destroy()


if __name__ == '__main__':
    main = Tk()
    app = Face_Recognition_System(main)
    main.mainloop()