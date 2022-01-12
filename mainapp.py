import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import sqlite3


class Start_menu:

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()
        
        
        self.label1 = Label(self.frame, text='Choose an option:' , bg = 'lightblue' , font = ('Arial', 16), width='1440',height='2')
        self.label1.pack()

        self.button1 = Button(self.frame, text='Create an account', width='100' , height = '4' , command=self.load_createUser_frame)
        self.button1.pack()

        self.button2 = Button(self.frame, text='Log in', width = '100', height='4' , command=self.load_loginUser_frame)
        self.button2.pack()

        self.quit_button = Button(self.frame, text='Quit', width='100', height='4', command=self.frame.quit)
        self.quit_button.pack()

    def load_createUser_frame(self):

        self.newWindow =  tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Register Account')
        self.newWindow.grab_set()
        self.app = Create_user(self.newWindow)
        
    
    def load_loginUser_frame(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Login')
        self.newWindow.grab_set()
        self.app = Login_user(self.newWindow)


class Login_user:
    
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

        self.button1 = Button(self.main, text='Login', command = self.loginUser)
        self.button1.pack()

        self.back_button = Button(self.main, text='Back', command = self.backButton)
        self.back_button.pack()
    
    def backButton(self):
        self.main.destroy()

    def load_mainWindow(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Main window')
        self.newWindow.grab_set()
        self.app = Main_menu(self.newWindow)

    def loginUser(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)

        conn = sqlite3.connect('program_database.db')
        c = conn.cursor()
        with conn:
            c.execute("SELECT username, password FROM users")
            result = c.fetchall()

        login = (username, password)
        user = False
        for row in result:
            if row == login:
                user = True
        
        if user:
            messagebox.showinfo("Success", 'Login successful')
            self.load_mainWindow()

        else:
            messagebox.showerror("Error", 'Username or password incorrect')
              

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

    def createNew(self, username, password):

        newUser = User(username, password)
        newUser.insert_newUser()

    def verify(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)
    
        if re.match('^(?![-._])(?!.*[_.-]{2})[\w.-]{4,20}(?<![-._])$', username):
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
                messagebox.showinfo('Success', 'User has been created')
            else:
                messagebox.showerror('Error!', 'Password should contain at least:\n1) One capital letter \n2) One special sharacter \n3) One number \n4) Length Should be 8-18')       
        else:
            messagebox.showerror('Error!', 'Username is too long/short! \nMust be between 4-20')


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def get_info(self):
        print(self.username, self.password)

    def insert_newUser(self):
        conn = sqlite3.connect('program_database.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO users(username, password) VALUES (:username, :password)", {'username': self.username, 'password': self.password})


class Main_menu:

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.titlelabel = Label(self.main, text='Please select an option below:', font = ('Arial', 20), width = '360', height = '1', bg = 'lightblue')
        self.titlelabel.pack()

        self.infolabel = Label(self.main, text = '(Start with Create class)', font = ('Arial', 8), width = '360', height = '1', bg = 'lightblue')
        self.infolabel.pack()

        self.spacelabel = Label(self.main, text='', height ='5')
        self.spacelabel.pack()

        self.createClass_button = Button(self.main, text = 'Create a class', width='10',height='2', command = self.load_createClass)
        self.createClass_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        self.addStudent_button = Button(self.main, text = 'Add student', width = '10', height = '2', command = self.load_addStudent)
        self.addStudent_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        self.viewClass_button = Button(self.main, text = 'View class', width = '10', height = '2', command = self.load_viewClass)
        self.viewClass_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        self.backButton = Button(self.main, text='Back', command = self.backButton)
        self.backButton.pack()

    def backButton(self):
        self.main.destroy()

    def load_createClass(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Create a class')
        self.newWindow.grab_set()
        self.app = Subjectclass(self.newWindow)

    def load_addStudent(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Add student')
        self.newWindow.grab_set()
        self.app = Student(self.newWindow)

    def load_viewClass(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.attributes('-fullscreen', True)
        self.newWindow.title('Add student')
        self.newWindow.grab_set()
        self.app = Viewsubjectclass(self.newWindow)


# Main focus right now

class Subjectclass:

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        self.mainlabel = Label(self.main, text='Create class', font=('Arial', 16), width='720', height='3', bg = 'lightblue')
        self.mainlabel.pack()

        self.infolabel = Label(self.main, text = 'Fill out details below to create class' , font =('Arial', 10), width='720', height='1', bg ='lightblue')
        self.infolabel.pack()

        self.blanklabel = Label(self.main, text ='')
        self.blanklabel.pack()

        self.subjectNamelabel = Label(self.main, text = 'Subject name *', fg = 'red')
        self.subjectNamelabel.pack()

        self.subjectList = ['Select subject ...',
                            'Biology',
                            'Business Studies',
                            'Chemistry',
                            'Computer Science',
                            'Maths',
                            'Physics',
                            'Psychology']

        self.subjectName = ttk.Combobox(self.main, value=self.subjectList)
        self.subjectName.current(0)
        self.subjectName.bind("<<CombobocSelected>>", self.notNULL)
        self.subjectName.pack()


        self.confirmButton = Button(self.main, text='Confirm', command = self.notNULL)
        self.confirmButton.pack()

    def notNULL(self):
        if self.subjectName.get() == 'Select subject ...':
            messagebox.showerror('Error', 'Please select a subject from the dropdown menu')
        

class Student:

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()


class Viewsubjectclass:

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()




if __name__ == "__main__":
    root = Tk()
    root.title('Start menu')
    root.attributes('-fullscreen', True)
    app =  Start_menu(root)
    root.mainloop()

