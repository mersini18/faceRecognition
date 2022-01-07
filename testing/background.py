from tkinter import *
from PIL import ImageTk,Image

root = Tk()


my_image = ImageTk.PhotoImage(Image.open('backgroundimg.png'))
label = Label(image = my_image)
label.pack()

root.mainloop()