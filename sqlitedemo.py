import sqlite3
from students import Student

conn = sqlite3.connect('student.db')

c = conn.cursor()

# c.execute("""CREATE TABLE students (
#             first text,
#             last text,
#             attendance integer
#             )""")   

def insert_stu(stu):
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :attendance)", {'first': stu.first, 'last': stu.last, 'attendance': stu.attendance})

def get_stu_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_attendance(stu, attendance):
    with conn:
        c.execute("""UPDATE students SET attendance = :attendance
                    WHERE first = :first AND last = :last""",
                    {'first': stu.first, 'last': stu.last, 'attendance': attendance})

def remove_stu(stu):
    with conn:
        c.execute("DELETE from students WHERE first = :first AND last = :last",
                    {'first': stu.first, 'last': stu.last})


stu_1 = Student("Daniel", "Trowbridge", 100)
stu_2 = Student("Abdou", "Naji", 63)



students = get_stu_by_name('Naji')
print(students)

update_attendance(stu_2, 70)

students = get_stu_by_name('Naji')
print(students)



conn.close()

