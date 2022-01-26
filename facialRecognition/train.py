from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import cv2
import numpy as np

class Train:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        self.trainButton = Button(self.main, text='Train data set', width=20, height=3) 
        self.trainButton.pack()

if __name__ == '__main__':
    main = Tk()
    app = Train(main)
    main.mainloop() 
