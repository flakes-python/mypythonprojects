import tkinter as tk
from tkinter import *
import random
def randomnum():
    b = textbox.get()
    c = textbox2.get()
    d = int(b)
    e = int(c)
    
    a = random.randint(d, e)
    textvar.set(a)


root = tk.Tk()
label = Label(root, text="Random Number Generator", font=("Arial", 13))
label.pack()
textvar = StringVar()
textvar.set("number here")
label2 = Label(root, textvariable=textvar)
textbox = Entry(root)
label3 = Label(root, text="To")
textbox2 = Entry(root)
button = Button(root, text="Click me", command=randomnum)
textbox.pack()
label3.pack()
textbox2.pack()
button.pack()
label2.pack()
root.mainloop()
