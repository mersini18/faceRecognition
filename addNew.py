#  Import SQLire library
import sqlite3

# Connect to database
conn = sqlite3.connect('program_database.db')

# Initialse cursor to perform acions with database
c = conn.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS users (
#             userID INTEGER PRIMARY KEY,   
#             username TEXT,
#             password TEXT
#             )""")

def insert_newUser(username, password):
    with conn:
        c.execute("INSERT INTO users(username,password) VALUES (:username, :password)", {'username': username, 'password': password})
# Creates the users table with two columns, username & password
# c.execute("""CREATE TABLE users (
#             username text, 
#             password text
#              )""")

# A function to insert the new users data in to the table 'users'
def insert_newUser(newUser):
    # With conn automatically commits and closes the connection with the database
    # once it has executed the following code
    with conn:
        # Inserts username and password in to its relevant columns within table
        c.execute("INSERT INTO users VALUES (:username, :password)", {'username': newUser.username, 'password': newUser.password})

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




# newUser = User(username, password)
# insert_newUser(newUser)



