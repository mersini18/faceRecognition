import sqlite3

conn = sqlite3.connect('programdatabase.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS student (
            studentID INTEGER PRIMARY KEY,   
            firstName TEXT,
            lastName TEXT,
            email TEXT,
            year INTEGER,
            tutor TEXT,
            subject TEXT,
            DOB TEXT,
            photo TEXT
            )""")

# self.studentData= ["StudentID",
#                             "First name",
#                             "Last name",
#                             "Year",
#                             "Tutor",
#                             "Email",
#                             "DOB",
#                             "Subject",
#                             "Photo"]
