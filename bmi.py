from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = Tk()
root.title("BODY MASS INDEX")
mylabel = Label(text="BODY MASS INDEX CALCULATOR").grid(row=0,column=0)

# Calculating BMI
def bmi():
    mass2 = mass.get()  # retrieving the input variable for mass
    h2 = h.get()        # retrieving height variable
    h2 = h2/100         
    bmi_calc = mass2/(h2*h2)    # formula
    
    calc.insert(0, bmi_calc)    # displayng the result

def mbox():
    var1 = h.get()
    if var1 == 0:
        tk.messagebox.showinfo("ALERT", 'Height can not be 0!!!')
  
def combined():
    mbox()
    bmi()       
    
mass = IntVar()     # initializing variable
h = IntVar()        # initializing variable

Label(text="WEIGHT").grid(row=1,column=0)

# input box
weight = Entry(textvariable=mass).grid(row=1,column=1)

Label(text="HEIGHT").grid(row=2,column=0)

# input box
height = Entry(textvariable=h).grid(row=2,column=1)

Label(text="BMI").grid(row=3,column=0)

# output box
calc = Entry()
calc.grid(row=3,column=1)

btn = Button(text="CALCULATE", command=combined).grid(row=4)

root.mainloop()