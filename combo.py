from tkinter import *
from tkinter import ttk

def select():
    Label(text="You chose: " + var1.get()).grid(row=1, column=1)

root = Tk()
root.title("Combo")

var1 = StringVar(value="Choose a fruit")

combo = ttk.Combobox(textvariable=var1)
combo['values'] = ('apple', 'banana', 'orange', 'granadilla', 'mango')
combo.grid(row=0, column=1)

ttk.Label(text="Select your fruit").grid(row=0, column=0)

btn = ttk.Button(text="CHOOSE", command=select).grid()

root.mainloop()