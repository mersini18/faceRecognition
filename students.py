#Object orientated programming

class Student:  #This is the class 'student'

    def __init__(self,fname, lname, age, attendance): #Initialization
            self.fname = fname
            self.lname = lname
            self.age = age
            self.attendance = attendance
            
    def get_name(self):
        return (self.fname , self.lname)

    def get_attendance(self):
        return self.attendance
    

class Course: 

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_attendance(self):
        value = 0
        for student in self.students:
            value += student.get_attendance()
        return value / len(self.students)



