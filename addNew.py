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

def read_usernames(username, password):
    with conn:
        c.execute("SELECT * FROM users")
        result = c.fetchall()
        # print (result)
    login = (username, password)
    print (login)
    for row in result:
        if row == login:
            print("Successful login")
        else:
            print("User not found")

   



class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def get_info(self):
        print(self.username, self.password)

username = input('Enter username: ')
password = input('Enter password: ')


# newUser = User(username, password)
# insert_newUser(newUser)

read_usernames(username, password)



