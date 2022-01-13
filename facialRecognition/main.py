
from tkinter import *
from tkinter import ttk
from student import Student


class Face_Recognition_System:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        self.titlelabel = Label(self.main, text = 'Facial Recognition Attendance System', width=100, height =3, font = ('Arial', 20), bg = 'lightblue')
        self.titlelabel.grid(row=0,column=0,columnspan=7)

        self.blank = Label(self.main, text = '', height = 2)
        self.blank.grid(row=1)

        self.addStudentbutton = Button(self.main, text = 'Student details',command = self.studentDetails, width=20, height=3)
        self.addStudentbutton.grid(row =2,column =2, columnspan=1)
        self.viewClassbutton = Button(self.main, text = 'View Class', width=20, height=3)
        self.viewClassbutton.grid(row =2,column =3, columnspan=1)
        self.attendancebutton = Button(self.main, text = 'Attendance', width=20, height=3)
        self.attendancebutton.grid(row =2,column =4, columnspan=1)

        self.blank = Label(self.main, text = '', height = 2)
        self.blank.grid(row=3)

        self.trainDatabutton = Button(self.main, text = 'Train Data', width=20, height=3)
        self.trainDatabutton.grid(row = 4,column =2, columnspan=1)
        self.openPhotos = Button(self.main, text = 'Photos', width=20, height=3)
        self.openPhotos.grid(row =4,column =3, columnspan=1)
        self.quitbutton = Button(self.main, text = 'Quit', width=20, height=3)
        self.quitbutton.grid(row =4,column =4, columnspan=1)

    # Functions buttons

    # Student details button
    def studentDetails(self):
        self.newWindow = Toplevel(self.main)
        self.app=Student(self.newWindow)


if __name__ == '__main__':
    main = Tk()
    app = Face_Recognition_System(main)
    main.mainloop()