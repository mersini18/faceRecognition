import csv
import os
import re
from tkinter import *


def register_user():    
    with open('user_info.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow([validate_username,validate_password])

    Label(reg_screen, text="Registration successful!", fg="green").pack()

def delete_incorrect_password_match_screen():
    incorrect_password_match_screen.destroy()

def incorrect_password_match():
    global incorrect_password_match_screen
    incorrect_password_match_screen = Toplevel(reg_screen)
    incorrect_password_match_screen.title("Error")
    incorrect_password_match_screen.geometry("150x100")

    Label(incorrect_password_match_screen, text="Passwords do not match", fg="Red").pack()
    Button(incorrect_password_match_screen, text="Ok", command=delete_incorrect_password_match_screen).pack()

def delete_invalid_password_screen():
    invalid_password_screen.destroy()

def invalid_password():
    global invalid_password_screen
    
    invalid_password_screen = Toplevel(reg_screen)
    invalid_password_screen.title("Error")
    invalid_password_screen.geometry("300x200")
    
    Label(invalid_password_screen, text="Invalid Password!", fg="red").pack()
    Label(invalid_password_screen, text="Should contain: \n\n1) One Capital Letter \n2) Special Character \n3) One Number \n4) Length Should be 8-18: ").pack()
    Button(invalid_password_screen, text="Ok", width="10", command=delete_invalid_password_screen).pack()

    
    
def register_verify():

    global validate_username
    global validate_password

    validate_username = username_entry.get()
    validate_password = password_entry.get()
    validate_confirm_password = confirm_password_entry.get()

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    confirm_password_entry.delete(0,END)
    

    reg_password =  "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    match_re_password = re.compile(reg_password)


    reg_username = "^[A-Za-z][A-Za-z0-9_.-]{7,29}$"
    match_re_username = re.compile(reg_username)
    
    if validate_password == validate_confirm_password:
        
        res = re.search(match_re_password, validate_password)
        if res:
            register_user()
        else:
            invalid_password()
    else:
        incorrect_password_match()
    
    
def register():
    global reg_screen
    reg_screen = Toplevel(start_menu)
    reg_screen.title("Register")
    reg_screen.geometry("1440x900")

    global username
    global password
    global confirm_password
    global username_entry
    global password_entry
    global confirm_password_entry
    
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()

    Label(reg_screen, text="Please enter details below").pack()
    Label(reg_screen, text="").pack()
    
    Label(reg_screen, text="Username *", fg="red").pack()
    username_entry = Entry(reg_screen, textvariable=username, bg='grey')
    username_entry.pack()

    Label(reg_screen, text="Password *", fg="red").pack()
    password_entry = Entry(reg_screen, textvariable=password, show='*', bg='grey')
    password_entry.pack()

    Label(reg_screen, text="Confirm password *", fg="red").pack()
    confirm_password_entry = Entry(reg_screen, textvariable=confirm_password, show='*', bg='grey')
    confirm_password_entry.pack()


    Label(reg_screen, text="").pack()
    Button(reg_screen, text="Register", height="2", width="30", command=register_verify).pack()

def delete_login_success():
    login_success_screen.destroy()
    

def login_success():
    global login_success_screen
    
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success", fg="Green").pack()

    Button(login_success_screen, text="Ok", width="10",command=delete_login_success).pack()

def delete_user_not_found():
    user_not_found_screen.destroy()

    
def user_not_found():
    global user_not_found_screen
    
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User not found", fg="Red").pack()
    Button(user_not_found_screen, text="Ok", command=delete_user_not_found).pack()
    
    
def login_verification():

    
    log_username = username_verify.get()
    log_password = password_verify.get()

    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    entry = [log_username,log_password]
    found = False
    with open("user_info.csv", "r") as file:
        content = csv.reader(file)
        for row in content:
            if entry == row:
                found = True
                break
        if found == True:
            login_success()
        else:
            user_not_found()
    
    
def login():
    global login_screen

    login_screen = Toplevel(start_menu)
    login_screen.title("Login")
    login_screen.geometry("1440x900")


    Label(login_screen, text="Please enter details below").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry    
    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username *", fg="red").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bg='grey')
    username_login_entry.pack()

    Label(login_screen, text="Password *", fg="red").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify,show ='*', bg='grey')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", height="2", width="30", command=login_verification).pack()


def start():
    global start_menu
    start_menu = Tk()
    start_menu.geometry("1440x900")
    start_menu.state("normal")
    start_menu.title("Account Login")
    #bg = PhotoImage(file = "bg.png")
    

    Label(text="Choose Login or Register", bg="grey", width="250", height="2").pack()
    Label(text="").pack()

    Button(text="Login", height="2", width="60", command=login).pack()
    Label(text="").pack()

    Button(text="Register", height="2", width="60", command=register).pack()
    Label(text="").pack()

    start_menu.mainloop()
    

    
start()
