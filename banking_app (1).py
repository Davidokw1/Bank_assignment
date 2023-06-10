from tkinter import *
import os
from PIL import ImageTk, Image




# Main Screen
main = Tk()
main.title("MANCHESTER BANK")
logo = PhotoImage(file="david.png")
main.iconphoto(True,logo)
main.config(background="#2A61AB")
main.geometry("300x500")


def savings():
    window = Tk()
    window.title("Savings Account")
    logo = PhotoImage(file="david.png")
    window.config(background="#2A61AB")
    window.geometry("300x500")
    Button(window, text="deposit").grid(row=1, column=1)
    Button(window, text="withdrawal").grid(row=2, column=1)
    Button(window, text="Balance", command=check_balance).grid(row=7,column=1)
    

def current():
    window = Tk()
    window.title("Current Account")
    logo = PhotoImage(file="david.png")
    window.config(background="#2A61AB")
    window.geometry("300x500")
    Button(window, text="deposit").grid(row=1, column=1)
    Button(window, text="withdrawal").grid(row=2, column=1)
    Button(window, text="Balance", command=check_balance).grid(row=7,column=1)

def check_balance():
    window = Tk()
    window.title("Balance")
    logo = PhotoImage(file="david.png")
    window.config(background="#2A61AB")
    window.geometry("300x500")
    Label(window, text="10000").grid(row=1, column=1)



Label(main, text="what type of Account do you have? ").grid(row=0, column=0)

Button(main, text="Savings", font=("calibri", 12), width=20, command=savings).grid(
    row=3, 
    )
Button(main, text="Current", font=("calibri", 12), width=20, command=current).grid(
    row=5, pady=10
    )




mainloop()
