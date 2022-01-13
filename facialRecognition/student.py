from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Student:

    def __init__(self, main):
        self.main = main
        self.main.geometry('1440x900')
        self.main.title('Face Secognition System')

        # Variables
        self.studentSubject = StringVar()
        self.studentYear = StringVar()
        self.studentTutor = StringVar()
        self.studentfirstName = StringVar()
        self.studentlastName = StringVar()
        self.studentEmail = StringVar()
        self.studentDOB = StringVar()
        self.radio1 = StringVar()
        self.radio2 = StringVar()


        self.titlelabel = Label(self.main, text = 'Student Management System', width=100, height =3, font = ('Arial', 20), bg = 'lightblue')
        self.titlelabel.grid(row=0,column=0,columnspan=7)

    # Left label frame

        self.leftFrame = LabelFrame(self.main, bd=2,relief=RIDGE, text ='Student Details', bg='white')
        self.leftFrame.place(x=5,y=100,width=700,height=775)

    # Student course frame

        self.subjectFrame = LabelFrame(self.leftFrame, bd=2 , bg='white', relief=RIDGE, text='Student subject information')
        self.subjectFrame.place(x=10,y=10,width=620,height=200)

        # Subjet information

        self.subjectLabel = Label(self.subjectFrame, text = 'Subject: ', bg='white')
        self.subjectLabel.grid(row=0,column=0,sticky=W)

        self.subjectList = ['Select subject',
                            'Biology',
                            'Business Studies',
                            'Chemistry',
                            'Computer Science',
                            'Maths',
                            'Physics',
                            'Psychology']

        self.subjectcombo = ttk.Combobox(self.subjectFrame, textvariable = self.studentSubject, value=self.subjectList, state = 'readonly')
        self.subjectcombo.current(0)
        self.subjectcombo.bind("<<CombobocSelected>>")
        self.subjectcombo.grid(row=0,column=1, padx=2,pady=10)

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

        self.yearcombo = ttk.Combobox(self.subjectFrame, textvariable=self.studentYear, value=self.yearList, state = 'readonly')
        self.yearcombo.current(0)
        self.yearcombo.bind("<<CombobocSelected>>")
        self.yearcombo.grid(row=1,column=1, padx=2,pady=10)

        # Tutor

        self.tutorLabel = Label(self.subjectFrame, text = 'Tutor group: ', bg='white')
        self.tutorLabel.grid(row=0,column=3,sticky=W)

        self.tutorList = ['Select tutor group',
                            'A',
                            'B',
                            'C',
                            'D',
                            'E',
                            'F',]

        self.tutorcombo = ttk.Combobox(self.subjectFrame, textvariable=self.studentTutor, value=self.tutorList, state = 'readonly')
        self.tutorcombo.current(0)
        self.tutorcombo.bind("<<CombobocSelected>>")
        self.tutorcombo.grid(row=0,column=4, padx=2,pady=10)

    # Student information frame

        self.studentFrame = LabelFrame(self.leftFrame, bd=2 , bg='white', relief=RIDGE, text='Enter student information below:')
        self.studentFrame.place(x=10,y=210,width=620,height=300)

        # First name label

        self.studentfirstName_label = Label(self.studentFrame, text = 'First name: ', bg='white')
        self.studentfirstName_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        self.studentfirstName_entry = ttk.Entry(self.studentFrame, textvariable=self.studentfirstName, width=20)
        self.studentfirstName_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Last name label

        self.studentlastName_label = Label(self.studentFrame, text = 'Last name: ', bg='white')
        self.studentlastName_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        self.studentlastName_entry = ttk.Entry(self.studentFrame, textvariable=self.studentlastName, width=20)
        self.studentlastName_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Email address

        self.studentEmail_label = Label(self.studentFrame, text = 'Email address: ', bg='white')
        self.studentEmail_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        self.studentEmail_entry = ttk.Entry(self.studentFrame, textvariable=self.studentEmail, width=30)
        self.studentEmail_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Date of birth

        self.studentDOB_label = Label(self.studentFrame, text = 'Date of birth: ', bg='white')
        self.studentDOB_label.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        self.studentDOB_entry = ttk.Entry(self.studentFrame, textvariable=self.studentDOB, width=20)
        self.studentDOB_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)

        # Radio buttons

        # Text variable removes text from button
        self.radiobutton1 = ttk.Radiobutton(self.studentFrame, text= 'Take photo sample', value = 'Yes')
        self.radiobutton1.grid(row=4,column=0, padx=2,pady=10, sticky=W)

        self.radiobutton2 = ttk.Radiobutton(self.studentFrame, text= 'No photo sample', value='No')
        self.radiobutton2.grid(row=4,column=1,padx=2,pady=10,sticky=W)
    
    # Buttons frame

        self.buttonFrame = Frame(self.studentFrame, bd=2, relief=RIDGE, bg='white')
        self.buttonFrame.place(x=0,y=200,width=615,height=80)

        # Submit Button
        self.submitButton = Button(self.buttonFrame, command=self.addData, text='Submit', width=15, bg='grey')
        self.submitButton.grid(row=0,column=0)

        # Update button
        self.updateButton = Button(self.buttonFrame, text='Update', width=15, bg='grey')
        self.updateButton.grid(row=0,column=1)

        # Reset button
        self.resetButton = Button(self.buttonFrame, text='Reset', width=15, bg='grey')
        self.resetButton.grid(row=0,column=2)

        # Take Photo
        self.takephotoButton = Button(self.buttonFrame, text='Take photo sample', width=15, bg='grey')
        self.takephotoButton.grid(row=0,column=3)

        # Update Photo
        self.updatephotoButton = Button(self.buttonFrame, text='Update photo', width=15, bg='grey')
        self.updatephotoButton.grid(row=0,column=4)


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
                            "Year",
                            "Tutor",
                            "Email",
                            "DOB",
                            "Subject",
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
        self.studentTable.column(self.studentData[3],width=100)
        self.studentTable.column(self.studentData[4],width=100)
        self.studentTable.column(self.studentData[5],width=100)
        self.studentTable.column(self.studentData[6],width=100)
        self.studentTable.column(self.studentData[7],width=100)
        self.studentTable.column(self.studentData[8],width=100)
        self.studentTable.pack(fill=BOTH,expand=1)


    # Function declaration

    def addData(self):
        if self.studentSubject.get() == 'Select subject':
            messagebox.showerror('Error', 'All fields are required', parent=self.main)
        elif self.studentYear.get() == 'Select year':
            messagebox.showerror('Error', 'All fields are required', parent=self.main)
        elif self.studentTutor.get() == 'Select tutor group':
            messagebox.showerror('Error', 'All fields are required', parent=self.main)
        else:
            messagebox.showinfo('Success', 'Student added', parent=self.main)


if __name__ == '__main__':
    main = Tk()
    app = Student(main)
    main.mainloop()