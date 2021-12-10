import sqlite3


conn = sqlite3.connect('program_database.db')

c = conn.cursor()

# c.execute("""CREATE TABLE users (
#             username text,
#             password text
#             )""")

def insert_newUser(newUser):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password)", {'username': newUser.username, 'password': newUser.password})


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def get_info(self):
        print(self.username, self.password)

username = input('Enter username: ')
password = input('Enter password: ')
password = hash(password)


newUser = User(username, password)

insert_newUser(newUser)