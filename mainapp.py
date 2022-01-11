import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import sqlite3

# Main window
class Start_menu:

    def __init__(self, main):
        # Create a frame for the window for formatting
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()
        
        # Label for main title of window
        self.label1 = Label(self.frame, text='Choose an option:' , bg = 'lightblue' , font = ('Arial', 16), width='1440',height='2')
        self.label1.pack()

        # Button to change to new window - create an account
        self.button1 = Button(self.frame, text='Create an account', width='100' , height = '4' , command=self.load_createUser_frame)
        self.button1.pack()

        # Button to change to a different window - login window
        self.button2 = Button(self.frame, text='Log in', width = '100', height='4' , command=self.load_loginUser_frame)
        self.button2.pack()

        # Quit button to exit the program
        self.quit_button = Button(self.frame, text='Quit', width='100', height='4', command=self.frame.quit)
        self.quit_button.pack()

    # Sets parameters for 'Create an account' window
    def load_createUser_frame(self):

        # Sets window as a toplevel of main window
        self.newWindow =  tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Register Account')
        self.newWindow.grab_set() # Restricts user access to just this window 
        self.app = Create_user(self.newWindow)
        
    
    def load_loginUser_frame(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Login')
        self.newWindow.grab_set()
        self.app = Login_user(self.newWindow)


# Class for login menu
class Login_user:
    
    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        # Main label of window
        self.label1 = Label(self.main, text = 'Enter details below:', font = ('Arial', 20), width = '720', height = '4', bg = 'lightblue')
        self.label1.pack()

        # Blank label to create space under title
        self.label2 = Label(self.main, text = '')
        self.label2.pack()

        # Label signifies information for entry widget below
        # Set to red which signifies a required field
        self.label3 = Label(self.main, text='Username *', fg = 'red')
        self.label3.pack()

        # Entry widget for user to input a userame
        # Stringvar is used by tkinter to store variables
        self.username = StringVar()
        self.username_entry = Entry(self.main, textvariable=self.username, bg = 'lightgrey')
        self.username_entry.pack()

        # Label widget for password
        self.label4 = Label(self.main, text='Password *' ,fg= 'red', )
        self.label4.pack()

        # User input through entry widget
        self.password = StringVar()
        self.password_entry = Entry(self.main, textvariable=self.password, show = '*', bg='lightgrey')
        self.password_entry.pack()

        # Login button
        self.button1 = Button(self.main, text='Login', command = self.loginUser)
        self.button1.pack()

        # Back button 
        self.back_button = Button(self.main, text='Back', command = self.backButton)
        self.back_button.pack()
    
    # Function to destroy current window - returns to main window
    def backButton(self):
        self.main.destroy()


    def load_mainWindow(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Main window')
        self.newWindow.grab_set()
        self.app = Main_menu(self.newWindow)


    # Log in user to from database
    def loginUser(self):

        # Retrieves inputted data from user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Deletes whatever was inputted into boxes for next use
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)

        # Connect to database
        conn = sqlite3.connect('program_database.db')
        c = conn.cursor()
        with conn:
            # Selects username and password from users tables
            c.execute("SELECT username, password FROM users")
            # Fetches all results
            result = c.fetchall()

        # Creates a tuple of username and password
        login = (username, password)

        user = False
        # For loop to iterate through results of database
        for row in result:
            if row == login:
                user = True
        
        # If user details are found
        if user:
            # Message displayed to user for successful login
            messagebox.showinfo("Success", 'Login successful')
            # Loads main window for user
            self.load_mainWindow()

        else:
            # Error message displayed to user
            messagebox.showerror("Error", 'Username or password incorrect')
              
# Create an account
class Create_user:

    def __init__(self, main):

        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        # Main label
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

    # Create user
    def createNew(self, username, password):

        # Username and password
        newUser = User(username, password)
        # Insert new user to database
        newUser.insert_newUser()

    # Validate username and password input
    def verify(self):
        # Retrive input from user for account creation
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Delete data from entry widgets
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)
    
        # Regex for username
        if re.match('^(?![-._])(?!.*[_.-]{2})[\w.-]{4,20}(?<![-._])$', username):
            specialSym =['$', '@', '#', '%']
            val = True

            # Success criteria for password
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

            # If password is valid
            if val:
                # Create new user with username and password
                self.createNew(username, password)
                # Display success message to user
                messagebox.showinfo('Success', 'User has been created')
            else:
                # Error message for invalid password
                messagebox.showerror('Error!', 'Password should contain at least:\n1) One capital letter \n2) One special sharacter \n3) One number \n4) Length Should be 8-18')       
        else:
            # Error message for invalid username
            messagebox.showerror('Error!', 'Username is too long/short! \nMust be between 4-20')

# Class for the user
class User:

    # Initialise the user
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # Print out username and password 
    def get_info(self):
        print(self.username, self.password)

    # Insert new user to SQL database
    def insert_newUser(self):
        conn = sqlite3.connect('program_database.db')
        c = conn.cursor()
        with conn:
            c.execute("INSERT INTO users(username, password) VALUES (:username, :password)", {'username': self.username, 'password': self.password})

# Main menu window
class Main_menu:

    def __init__(self, main):
        self.main = main
        self.frame = Frame(self.main)
        self.frame.pack()

        # Main title
        self.titlelabel = Label(self.main, text='Please select an option below:', font = ('Arial', 20), width = '360', height = '1', bg = 'lightblue')
        self.titlelabel.pack()

        # Helpful information
        self.infolabel = Label(self.main, text = '(Start with Create class)', font = ('Arial', 8), width = '360', height = '1', bg = 'lightblue')
        self.infolabel.pack()

        # Blank label
        self.spacelabel = Label(self.main, text='', height ='5')
        self.spacelabel.pack()

        # Create class button
        self.createClass_button = Button(self.main, text = 'Create a class', width='10',height='2', command = self.load_createClass)
        self.createClass_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        # Add student to class button
        self.addStudent_button = Button(self.main, text = 'Add student', width = '10', height = '2', command = self.load_addStudent)
        self.addStudent_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        # View class button
        self.viewClass_button = Button(self.main, text = 'View class', width = '10', height = '2', command = self.load_viewClass)
        self.viewClass_button.pack()

        self.spacelabel = Label(self.main, text='', height ='2')
        self.spacelabel.pack()

        # Back button
        self.backButton = Button(self.main, text='Back', command = self.backButton)
        self.backButton.pack()

    def backButton(self):
        self.main.destroy()

    def load_createClass(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Create a class')
        self.newWindow.grab_set()
        self.app = Subjectclass(self.newWindow)

    def load_addStudent(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
        self.newWindow.title('Add student')
        self.newWindow.grab_set()
        self.app = Student(self.newWindow)

    def load_viewClass(self):
        self.newWindow = tk.Toplevel(self.main)
        self.newWindow.geometry('1440x900')
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

        # List of subjects
        self.subjectList = ['Select subject ...',
                            'Biology',
                            'Business Studies',
                            'Chemistry',
                            'Computer Science',
                            'Maths',
                            'Physics',
                            'Psychology']

        # Combobox allowing user to select subject from drop down bar
        self.subjectName = ttk.Combobox(self.main, value=self.subjectList, state='readonly')
        # Sets dropdown to first item in list
        self.subjectName.current(0)
        self.subjectName.bind("<<CombobocSelected>>", self.notNULL)
        self.subjectName.pack()


        self.confirmButton = Button(self.main, text='Confirm', command = self.notNULL)
        self.confirmButton.pack()

    # Function to check if a subject has been selected
    def notNULL(self):
        if self.subjectName.get() == 'Select subject ...':
            # Error displayed to user
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
    root.geometry('1440x900')
    app =  Start_menu(root)
    root.mainloop()

