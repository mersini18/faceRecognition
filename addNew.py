import sqlite3


conn = sqlite3.connect('program_database.db')

c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS users (
#             userID INTEGER PRIMARY KEY,   
#             username TEXT,
#             password TEXT
#             )""")

def insert_newUser(username, password):
    with conn:
        c.execute("INSERT INTO users(username,password) VALUES (:username, :password)", {'username': username, 'password': password})

def deleteUser():
    with conn:
        c.execute("DELETE FROM users WHERE userID=4")

username = input("Username: ")
password = input("Password: ")

insert_newUser(username, password)

def selectUsers():
    with conn:
        c.execute("SELECT username, password FROM users")
        result = c.fetchall()
        print(result)







