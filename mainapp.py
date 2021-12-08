import tkinter as tk
from tkinter import *
import re

class Main_window:

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()
        
        
        self.label1 = Label(self.frame, text='Choose an option:' , bg = 'lightblue' , font = ('Arial', 16), width='1440',height='2')
        self.label1.pack()

        self.button1 = Button(self.frame, text='Create an account', width='100' , height = '4' , command=self.load_createUser)
        self.button1.pack()

        self.button2 = Button(self.frame, text='Log in', width = '100', height='4' , command=self.login_user)
        self.button2.pack()

        self.quit_button = Button(self.frame, text='Quit', width='100', height='4', command=self.frame.quit)
        self.quit_button.pack()

    def load_createUser(self):

        self.newWindow =  tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Register Account')
        self.newWindow.grab_set()
        self.app = Create_user(self.newWindow)
        
    
    def login_user(self):
        pass

class Create_user:

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.label1 = Label(self.main, text = 'Enter details below:', font = ('Arial', 20), width = '720', height = '4', bg = 'lightblue')
        self.label1.pack()

        self.label2 = Label(self.main, text = '')
        self.label2.pack()

        self.label3 = Label(self.main, text='Username *', fg = 'red')
        self.label3.pack()

        self.username = StringVar()
        self.username_entry = Entry(self.main, textvariable=self.username, bg = 'lightgrey')
        self.username_entry.pack()

        self.label4 = Label(self.main, text='Password *' ,fg= 'red', )
        self.label4.pack()

        self.password = StringVar()
        self.password_entry = Entry(self.main, textvariable=self.password, show = '*', bg='lightgrey')
        self.password_entry.pack()
        
        self.register_button = Button(self.main, text='Confirm register', command=self.verify)
        self.register_button.pack()

        self.back_button = Button(self.main, text='Back', command=self.backButton)
        self.back_button.pack()

    def backButton(self):
        self.main.destroy()

    def verify(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)

        reg_password =  "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        reg_username = "^[A-Za-z][A-Za-z0-9_.-]{7,29}$"
        
        match_re_username = re.compile(reg_username)
        match_re_password = re.compile(reg_password)
        
        
        print(username, password)



    def load_createdUser(self):
        print(self.username_entry, self.password_entry)
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Success')
        self.newWindow.grab_set()
        self.app = Created(self.newWindow)

class Created:
        
    def __init__(self,main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()
            
        self.label1 = Label(self.main, text='Successfully created user!', fg = 'green', font=('Arial', 36))
        self.label1.pack()

        self.back_button = Button(self.main, text='Ok', width='50', height='2', command = self.backButton)            
        self.back_button.pack()
    
    def backButton(self):
        self.main.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title('Main menu')
    root.geometry('1440x900')
    app =  Main_window(root)
    root.mainloop()

