import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re
import sqlite3


class Main_window:

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()
        
        
        self.label1 = Label(self.frame, text='Choose an option:' , bg = 'lightblue' , font = ('Arial', 16), width='1440',height='2')
        self.label1.pack()

        self.button1 = Button(self.frame, text='Create an account', width='100' , height = '4' , command=self.load_createUser_frame)
        self.button1.pack()

        self.button2 = Button(self.frame, text='Log in', width = '100', height='4' , command=self.login_user)
        self.button2.pack()

        self.quit_button = Button(self.frame, text='Quit', width='100', height='4', command=self.frame.quit)
        self.quit_button.pack()

    def load_createUser_frame(self):

        self.newWindow =  tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Register Account')
        self.newWindow.grab_set()
        self.app = Create_user_frame(self.newWindow)
        
    
    def login_user(self):
        pass


class Create_user_frame:

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


    def load_createdUser_frame(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Success')
        self.newWindow.grab_set()
        self.app = Created_frame(self.newWindow)

    def load_usernameFail_frame(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('300x200')
        self.newWindow.title('Create user failed')
        self.newWindow.grab_set()
        self.app = usernameFail_frame(self.newWindow)

    def load_passwordFail_frame(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('300x200')
        self.newWindow.title('Create user failed')
        self.newWindow.grab_set()
        self.app = passwordFail_frame(self.newWindow)

    def createNew(self, username, password):

        password = hash(password)
        newUser = User(username, password)
        newUser.get_info()

    def verify(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)
    
    
      
        if re.match('^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$', username):
            specialSym =['$', '@', '#', '%']
            val = True
        
            if len(password) < 6:
                val = False
            
            if len(password) > 20:
                val = False
            
            if not any(char.isdigit() for char in password):
                val = False
                
            if not any(char.isupper() for char in password):
                val = False
                
            if not any(char.islower() for char in password):
                val = False
                
            if not any(char in specialSym for char in password):
                val = False

            if val:
                self.createNew(username, password)
                self.load_createdUser_frame()
            else:
                self.load_passwordFail_frame()
                
        else:
            self.load_usernameFail_frame()


class Created_frame:
        
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


class usernameFail_frame:

    def __init__(self,main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.label1 = Label(self.main, text='Username is too long/short! \nMust be between 4-20', font=('Arial', 36))
        self.label1.pack()

        self.back_button = Button(self.main, text='Ok', width='50', height='2', command = self.backButton)            
        self.back_button.pack()

    def backButton(self):
        self.main.destroy()  


class passwordFail_frame:

    def __init__(self,main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.label1 = Label(self.main, text ='Invalid Password!', fg='red', font=('Arial', 16))
        self.label1.pack()

        self.label2 = Label(self.main, text = 'Should contain at least: \n\n1) One cpital letter \n2) One special sharacter \n3) One number \n4) Length Should be 8-18: ')
        self.label2.pack()

        self.back_button = Button(self.main, text='Ok', width='50', height='2', command = self.backButton)
        self.back_button.pack()

    def backButton(self):
        self.main.destroy()


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def get_info(self):
        print(self.username, self.password)

    def addUser(self):
        #add user to database
        pass


if __name__ == "__main__":
    root = Tk()
    root.title('Main menu')
    root.geometry('1440x900')
    app =  Main_window(root)
    root.mainloop()

