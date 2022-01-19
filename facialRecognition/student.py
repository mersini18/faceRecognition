from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import cv2


class Student:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        self.titlelabel = Label(self.main, text = 'Student Management System', width=100, height =3, font = ('Arial', 20), bg = 'lightblue')
        self.titlelabel.grid(row=0,column=0,columnspan=7)

    # Left label frame

        self.leftFrame = LabelFrame(self.main, bd=2,relief=RIDGE, text ='Student Details', bg='white')
        self.leftFrame.place(x=5,y=100,width=700,height=775)

    # Student course frame

        self.subjectFrame = LabelFrame(self.leftFrame, bd=2 , bg='white', relief=RIDGE, text='Student subject information')
        self.subjectFrame.place(x=10,y=10,width=620,height=150)

        # Subjet information

        # Student ID

        self.studentIDlabel = Label(self.subjectFrame, text = 'StudentID: ', bg='white')
        self.studentIDlabel.grid(row=0,column=0,sticky=W)

        self.studentID = StringVar()
        self.studentID_entry = ttk.Entry(self.subjectFrame, textvariable=self.studentID, width=20, state='readonly')
        self.studentID_entry.grid(row=0,column=1,padx=2,pady=10)

        self.subjectLabel = Label(self.subjectFrame, text = 'Subject: ', bg='white')
        self.subjectLabel.grid(row=0,column=2,sticky=W)

        self.subjectList = ['Select subject',
                            'Biology',
                            'Business Studies',
                            'Chemistry',
                            'Computer Science',
                            'Maths',
                            'Physics',
                            'Psychology']

        self.subjectCombo = ttk.Combobox(self.subjectFrame, value=self.subjectList, state = 'readonly')
        self.subjectCombo.current(0)
        self.subjectCombo.bind("<<CombobocSelected>>")
        self.subjectCombo.grid(row=0,column=3, padx=2,pady=10)

        #  Year
        self.yearLabel = Label(self.subjectFrame, text = 'Year: ', bg='white')
        self.yearLabel.grid(row=1,column=0,sticky=W)

        self.yearList = ['Select year',
                            '7',
                            '8',
                            '9',
                            '10',
                            '11',
                            '12',
                            '13']

        self.yearCombo = ttk.Combobox(self.subjectFrame, value=self.yearList, state = 'readonly')
        self.yearCombo.current(0)
        self.yearCombo.bind("<<CombobocSelected>>")
        self.yearCombo.grid(row=1,column=1, padx=2,pady=10)

        # Tutor

        self.tutorLabel = Label(self.subjectFrame, text = 'Tutor group: ', bg='white')
        self.tutorLabel.grid(row=1,column=2,sticky=W)

        self.tutorList = ['Select tutor group',
                            'A',
                            'B',
                            'C',
                            'D',
                            'E',
                            'F',]

        self.tutorCombo = ttk.Combobox(self.subjectFrame, value=self.tutorList, state = 'readonly')
        self.tutorCombo.current(0)
        self.tutorCombo.bind("<<CombobocSelected>>")
        self.tutorCombo.grid(row=1,column=3, padx=2,pady=10)

        
    # Student information frame

        self.studentFrame = LabelFrame(self.leftFrame, bd=2 , bg='white', relief=RIDGE, text='Enter student information below:')
        self.studentFrame.place(x=10,y=160,width=650,height=400)

        # First name label

        self.studentfirstName_label = Label(self.studentFrame, text = 'First name: ', bg='white')
        self.studentfirstName_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        self.studentfirstName = StringVar()
        self.studentfirstName_entry = ttk.Entry(self.studentFrame, textvariable=self.studentfirstName, width=20)
        self.studentfirstName_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Last name label

        self.studentlastName_label = Label(self.studentFrame, text = 'Last name: ', bg='white')
        self.studentlastName_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        self.studentlastName = StringVar()
        self.studentlastName_entry = ttk.Entry(self.studentFrame, textvariable=self.studentlastName, width=20)
        self.studentlastName_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Email address

        self.studentEmail_label = Label(self.studentFrame, text = 'Email address: ', bg='white')
        self.studentEmail_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        self.studentEmail = StringVar()
        self.studentEmail_entry = ttk.Entry(self.studentFrame, textvariable=self.studentEmail, width=30)
        self.studentEmail_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Date of birth

        self.studentDOB_label = Label(self.studentFrame, text = 'Date of birth: ', bg='white')
        self.studentDOB_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        self.studentDOB = StringVar()
        self.studentDOB_entry = ttk.Entry(self.studentFrame, textvariable=self.studentDOB, width=20)
        self.studentDOB_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # Radio buttons

        # set as text variable and they dont work!!!!
        
        self.studentPhoto = StringVar()

        self.radiobutton1 = ttk.Radiobutton(self.studentFrame, variable=self.studentPhoto, text= 'Take photo sample', value = 'Yes')
        self.radiobutton1.grid(row=4,column=0, padx=2,pady=10, sticky=W)

        self.radiobutton2 = ttk.Radiobutton(self.studentFrame, variable=self.studentPhoto, text= 'No photo sample', value='No')
        self.radiobutton2.grid(row=4,column=1,padx=2,pady=10,sticky=W)
    
    # Buttons frame

        self.buttonFrame = Frame(self.studentFrame, bd=2, relief=RIDGE, bg='white')
        self.buttonFrame.place(x=0,y=300,width=645,height=80)

        # Submit Button
        self.submitButton = Button(self.buttonFrame, command = self.addData, text='Submit', width=10, bg='grey')
        self.submitButton.grid(row=0,column=0)

        # Update button
        self.updateButton = Button(self.buttonFrame, text='Update', command=self.updateStudent, width=10, bg='grey')
        self.updateButton.grid(row=0,column=1)

        # Delete button
        self.deleteButton = Button(self.buttonFrame, text = 'Delete', command=self.deleteData, width=10, bg='grey')
        self.deleteButton.grid(row=0,column=2)

        # Clear data button
        self.resetButton = Button(self.buttonFrame, text='Reset', command=self.clearData, width=10, bg='grey')
        self.resetButton.grid(row=0,column=3)

        # Take Photo
        self.takephotoButton = Button(self.buttonFrame, text='Take photo sample', command=self.generateDataset, width=15, bg='grey')
        self.takephotoButton.grid(row=1,column=0)

        # Update photo sample
        self.updatePhotobutton = Button(self.buttonFrame, text='Update photo', width=15, bg='grey')
        self.updatePhotobutton.grid(row=1,column=1)


    # Right label frame

        self.rightFrame = LabelFrame(self.main, bd=2,relief=RIDGE, text ='Student Details', bg='white')
        self.rightFrame.place(x=730,y=100,width=705,height=775)

    # Search system frame

        self.searchFrame = LabelFrame(self.rightFrame, bd=2 , bg='white', relief=RIDGE, text='Search System')
        self.searchFrame.place(x=10,y=10,width=680,height=65)

        # Search label
        self.searchLabel = Label(self.searchFrame, text = 'Search by: ', bg='white')
        self.searchLabel.grid(row=0,column=0,padx=2,pady=10,sticky=W)


        # Search by list
        self.searchData = ['Select',
                            'Student ID',
                            'First name',
                            'Last name',
                            'Email',
                            'Year',
                            'Tutor']


        # Search combobox
        self.searchcombo = ttk.Combobox(self.searchFrame, value=self.searchData, state = 'readonly')
        self.searchcombo.current(0)
        self.searchcombo.bind("<<CombobocSelected>>")
        self.searchcombo.grid(row=0,column=1)

        # Search entry
        self.search_entry = ttk.Entry(self.searchFrame, width=20)
        self.search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        
        # Search button
        self.searchButton = Button(self.searchFrame, text='Search', width = 15)
        self.searchButton.grid(row=0,column=3, padx=10,pady=10)

    # Search table frame

        self.tableFrame = LabelFrame(self.rightFrame, bd=2 , bg='white', relief=RIDGE, text='Search Results')
        self.tableFrame.place(x=10,y=75,width=680,height=200)

        self.scrollX = ttk.Scrollbar(self.tableFrame, orient=HORIZONTAL)
        self.scrollY = ttk.Scrollbar(self.tableFrame, orient=VERTICAL)

    # Student data liast
        self.studentData= ["StudentID",
                            "First name",
                            "Last name",
                            "Email",
                            "Year",
                            "Tutor",
                            "Subject",
                            "DOB",
                            "Photo"]

        # Initialise table through Treeview
        self.studentTable = ttk.Treeview(self.tableFrame,column=(self.studentData),xscrollcommand=self.scrollX.set,yscrollcommand=self.scrollY.set)
        
        # Create scrollbars for table
        self.scrollX.pack(side=BOTTOM, fill=X)
        self.scrollY.pack(side=RIGHT, fill=Y)
        self.scrollX.config(command=self.studentTable.xview)
        self.scrollY.config(command=self.studentTable.yview)
        
        # Set headings for Treeview student table
        self.studentTable.heading(self.studentData[0], text=self.studentData[0])
        self.studentTable.heading(self.studentData[1], text=self.studentData[1])
        self.studentTable.heading(self.studentData[2], text=self.studentData[2])
        self.studentTable.heading(self.studentData[3], text=self.studentData[3])
        self.studentTable.heading(self.studentData[4], text=self.studentData[4])
        self.studentTable.heading(self.studentData[5], text=self.studentData[5])
        self.studentTable.heading(self.studentData[6], text=self.studentData[6])
        self.studentTable.heading(self.studentData[7], text=self.studentData[7])
        self.studentTable.heading(self.studentData[8], text=self.studentData[8])
        self.studentTable["show"]="headings"

        # Resize the size of the heading
        self.studentTable.column(self.studentData[0],width=100)
        self.studentTable.column(self.studentData[1],width=100)
        self.studentTable.column(self.studentData[2],width=100)
        self.studentTable.column(self.studentData[3],width=200)
        self.studentTable.column(self.studentData[4],width=100)
        self.studentTable.column(self.studentData[5],width=100)
        self.studentTable.column(self.studentData[6],width=150)
        self.studentTable.column(self.studentData[7],width=100)
        self.studentTable.column(self.studentData[8],width=100)
        self.studentTable.pack(fill=BOTH,expand=1)
        self.studentTable.bind("<ButtonRelease>",self.getCursor)
        self.fetchData()
 

    # Function declaration

    def addData(self):

        # Ensure all fields have been entered
        self.inputError = False
        if self.subjectCombo.get() == 'Select subject':
            self.inputError = True
        elif self.yearCombo.get() == 'Select year':
            self.inputError = True
        elif self.tutorCombo.get() == 'Select tutor group':
            self.inputError = True
        elif self.studentfirstName.get() == '':
            self.inputError = True
        elif self.studentlastName.get() == '':
            self.inputError = True
        elif self.studentEmail.get() == '':
            self.inputError = True
        elif self.studentDOB.get() == '':
            self.inputError = True

        if self.inputError == True:
            messagebox.showerror("Error", "All fields must be answered")
        else:
            try:
                # Create connection to database
                conn =  sqlite3.connect('programdatabase.db')
                c = conn.cursor()
                with conn:
                    # Insert student entry to database
                    c.execute("""INSERT INTO student(firstName,lastName,email,year,tutor,subject,DOB,photo) 
                                                    VALUES (:firstName, 
                                                            :lastName, 
                                                            :email,
                                                            :year,
                                                            :tutor,
                                                            :subject,
                                                            :DOB,
                                                            :photo)""", 
                                                            {'firstName': self.studentfirstName.get(),
                                                            'lastName': self.studentlastName.get(),
                                                            'email': self.studentEmail.get(),
                                                            'year': self.yearCombo.get(),
                                                            'tutor': self.tutorCombo.get(),
                                                            'subject': self.subjectCombo.get(),
                                                            'DOB': self.studentDOB.get(),
                                                            'photo': self.studentPhoto.get()})
                self.fetchData()
                messagebox.showinfo("Success", "Student saved ")
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}")
                
    # Search table

    def fetchData(self):
        conn = sqlite3.connect("programdatabase.db")
        c = conn.cursor()
        with conn:
            c.execute("SELECT * FROM student")
        fetchResult = c.fetchall()

        if len(fetchResult) != 0:
            self.studentTable.delete(*self.studentTable.get_children())
            for i in fetchResult:
                self.studentTable.insert("", END, values=i)

    # Import from database

    def getCursor(self,event=""):
        cursorFocus = self.studentTable.focus()
        content = self.studentTable.item(cursorFocus)
        fetchResult=content["values"]

        self.studentID.set(fetchResult[0])
        self.studentfirstName.set(fetchResult[1])
        self.studentlastName.set(fetchResult[2])
        self.studentEmail.set(fetchResult[3])
        self.yearCombo.set(fetchResult[4])
        self.tutorCombo.set(fetchResult[5])
        self.subjectCombo.set(fetchResult[6])
        self.studentDOB.set(fetchResult[7])
        self.studentPhoto.set(fetchResult[8])

    #  Update button function

    def updateStudent(self):

         # Ensure all fields have been entered
        self.inputError = False
        if self.subjectCombo.get() == 'Select subject':
            self.inputError = True
        elif self.yearCombo.get() == 'Select year':
            self.inputError = True
        elif self.tutorCombo.get() == 'Select tutor group':
            self.inputError = True
        elif self.studentfirstName.get() == '':
            self.inputError = True
        elif self.studentlastName.get() == '':
            self.inputError = True
        elif self.studentEmail.get() == '':
            self.inputError = True
        elif self.studentDOB.get() == '':
            self.inputError = True

        if self.inputError == True:
            messagebox.showerror("Error", "All fields must be answered")
        else:
            try:
                # Ask user for input
                update = messagebox.askyesno("Update","Do you want to update these details")
                if update>0:
                    conn = sqlite3.connect("programdatabase.db")
                    c = conn.cursor()
                    with conn:
                        # create userID column
                        # update student details with new values
                        c.execute("""UPDATE student SET firstName = :firstName,
                                                        lastName = :lastName,
                                                        email = :email,
                                                        year = :year,
                                                        tutor = :tutor,
                                                        subject = :subject,
                                                        DOB = :DOB,
                                                        photo = :photo
                                                        WHERE studentID = :studentID""",
                                                        {'studentID': self.studentID.get(),
                                                        'firstName': self.studentfirstName.get(),
                                                        'lastName': self.studentlastName.get(),
                                                        'email': self.studentEmail.get(),
                                                        'year': self.yearCombo.get(),
                                                        'tutor': self.tutorCombo.get(),
                                                        'subject': self.subjectCombo.get(),
                                                        'DOB': self.studentDOB.get(),
                                                        'photo': self.studentPhoto.get()})
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student update successful")
                self.fetchData()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}")

    # Delete function
    def deleteData(self):
        try:
            delete = messagebox.askyesno("Delete Student", 'Would you like to remove this student')
            if delete>0:
                conn = sqlite3.connect("programdatabase.db")
                c = conn.cursor()
                with conn:
                    c.execute("DELETE FROM student WHERE studentID = :studentID", {'studentID': self.studentID.get()})
            else:
                if not delete:
                    return
            messagebox.showinfo("Delete", "Student successfully deleted")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}")

    # Clear boxes function
    def clearData(self):
        self.studentID.set('')
        self.subjectCombo.set('Select subject')
        self.yearCombo.set('Select year')
        self.tutorCombo.set('Select tutor group')
        self.studentfirstName.set('')
        self.studentlastName.set('')
        self.studentEmail.set('')
        self.studentDOB.set('')
        self.studentPhoto.set('')

    # Take photo samples

    def generateDataset(self):
        
        self.inputError = False
        if self.subjectCombo.get() == 'Select subject':
            self.inputError = True
        elif self.yearCombo.get() == 'Select year':
            self.inputError = True
        elif self.tutorCombo.get() == 'Select tutor group':
            self.inputError = True
        elif self.studentfirstName.get() == '':
            self.inputError = True
        elif self.studentlastName.get() == '':
            self.inputError = True
        elif self.studentEmail.get() == '':
            self.inputError = True
        elif self.studentDOB.get() == '':
            self.inputError = True

        if self.inputError == True:
            messagebox.showerror("Error", "All fields must be answered")
        else:
            try:
                conn = sqlite3.connect('programdatabase.db')
                c = conn.cursor()
                
                c.execute('SELECT * FROM student')
                result = c.fetchall()
                id = 0
                for x in result:
                    id +=1  
                    c.execute("""UPDATE student SET firstName = :firstName,
                                                    lastName = :lastName,
                                                    email = :email,
                                                    year = :year,
                                                    tutor = :tutor,
                                                    subject = :subject,
                                                    DOB = :DOB,
                                                    photo = :photo
                                                    WHERE studentID = :studentID""",
                                                    {'studentID': self.studentID.get()==id+1,
                                                    'firstName': self.studentfirstName.get(),
                                                    'lastName': self.studentlastName.get(),
                                                    'email': self.studentEmail.get(),
                                                    'year': self.yearCombo.get(),
                                                    'tutor': self.tutorCombo.get(),                                                        'subject': self.subjectCombo.get(),
                                                    'DOB': self.studentDOB.get(),
                                                    'photo': self.studentPhoto.get()})
                conn.commit()
                self.fetchData()
                self.clearData()  
                conn.close()              

                # Load predefined face

                
                faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")                    
                
                def faceCropped(frame):
            
                    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
                    # scaling factor = 1.3
                    # minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        faceCropped=frame[y:y+h, x:x+w]
                        return faceCropped
                    
                cap = cv2.VideoCapture(0)
                imgID = 0
                while True:
                    ret, frame = cap.read()                        
                    if faceCropped(frame) is not None:
                        imgID +=1
                    face = cv2.resize(faceCropped(frame),(450, 450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    filenamePath = "data/user."+str(id)+"."+str(imgID)+".jpg"
                    cv2.imwrite(filenamePath, face)
                    cv2.putText(face,str(imgID),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1) == 13 or int(imgID)==30:
                        break
                    
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset complete")


            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}")



if __name__ == '__main__':
    main = Tk()
    app = Student(main)
    main.mainloop() 
