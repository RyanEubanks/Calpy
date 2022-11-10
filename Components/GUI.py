from tkinter import *
from tkinter.ttk import *

# root is the main window object
root = Tk()

# window size
root.geometry("800x500")

# setting the title of the main window
root.title("CalPy")

# simple display of Hello, World; pack is a layout
label = Label(root, text="Hello, World", font=('Arial', 18)).pack(padx=20,pady=20)

"""
textbox = Text(root, height= 5, font=('Arial', 16)).pack()

# entry is not multi-line enabled
entry = Entry(root).pack(padx=10)

button = Button(root, text="click", font=("Arial", 15)).pack(padx=10, pady=10)
"""

##################   actual implementation of the GUI    ############################
buttonFrame = Frame(root)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

btn1 = Button(buttonFrame, text="1").grid(row=0, column=0).c



root.mainloop()