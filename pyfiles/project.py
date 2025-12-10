import tkinter as tk
from tkinter import *
import random

def rannum():
    a = random.randint(1, 3)
    if a == 1:
        returnback.set("Paper")
    elif a == 2:
        returnback.set("Rock")
    else:
        returnback.set("Scissors")
    return a

def go():
    answer()

def answer():
    y = b.get()
    a = rannum()  # Generate new random number each time
    
    # 0 = Paper, 1 = Scissors, 2 = Rock
    # Paper beats Rock, Rock beats Scissors, Scissors beats Paper
    
    if y == 0:  # Player chose Paper
        if a == 2:  # AI chose Rock
            mamamia.set("You Win!!")
        elif a == 1:  # AI chose Paper
            mamamia.set("It's a Tie!!")
        else:  # AI chose Scissors
            mamamia.set("You Lose!!")
            
    elif y == 1:  # Player chose Scissors
        if a == 1:  # AI chose Paper
            mamamia.set("You Win!!")
        elif a == 3:  # AI chose Scissors
            mamamia.set("It's a Tie!!")
        else:  # AI chose Rock
            mamamia.set("You Lose!!")
            
    elif y == 2:  # Player chose Rock
        if a == 3:  # AI chose Scissors
            mamamia.set("You Win!!")
        elif a == 2:  # AI chose Rock
            mamamia.set("It's a Tie!!")
        else:  # AI chose Paper
            mamamia.set("You Lose!!")

root = tk.Tk()
root.title("Rock Paper Scissors")

returnback = StringVar()
returnback.set("AI's Answer here")
mamamia = StringVar()
mamamia.set("...")

# Create UI elements
returnbackstr = Label(root, textvariable=returnback, font=("Arial", 14))
mamamiastr = Label(root, textvariable=mamamia, font=("Arial", 16, "bold"))
gay = Button(root, text="Go!!", command=go, font=("Arial", 12))
credits = Label(root, text="Made By flakes (2025)")
selection = ["Paper", "Scissors", "Rock"]
b = IntVar()
b.set(0)  # Set default selection

# Pack elements in correct order
Label(root, text="Choose your move:", font=("Arial", 12)).pack(pady=10)

for index in range(len(selection)):
    x = Radiobutton(root, text=selection[index], variable=b, value=index, font=("Arial", 11))
    x.pack()

gay.pack(pady=10)
returnbackstr.pack(pady=5)
mamamiastr.pack(pady=5)
credits.pack()

root.mainloop()
