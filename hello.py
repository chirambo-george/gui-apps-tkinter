import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("HELLO WORLD")

# HOW TO ADD SECOND WINDOW
# mywin = tk.Tk()
# mywin.title("SECOND WINDOW")
# mywin.geometry('500x500+600+0')


# hello = tk.Label(root, text="HELLO WORLD", bg='red').pack()
root.geometry('500x500+0+0')
# ADDING FUNCTIONALITY TO A BUTTON
# def btnfn():
#     Label(text="BUTTON FUNCTIONALITY ADDED").pack()
    
txt = StringVar()
# a = IntVar()
mytext = Entry(textvariable = txt).pack() 


def btnfn2():
    txt1 = txt.get()
    mylabel = tk.Label(root, text=txt1).pack()

def gui():
    fn = tk.Tk()
    fn.title("NEW PROJECT")
    fn.geometry("400x400+600+0")
    fn.mainloop()
    
# ******** MESSAGE BOX **********


def mbox():
    tk.messagebox.showinfo("SAVE", 'Do you want to save this file?')
    
def close():
    mess = tk.messagebox.askquestion("CLOSE", 'Do you want to close this file?')
    if mess == 'yes':
        return exit()
        # root.destroy() # another way to do it

    
button = tk.Button(text="Submit", command=btnfn2).pack()

# ********** MENU & FUNCTIONALITY **********
options = Menu()
dropdown = Menu()
dropdown.add_command(label="NEW PROJECT", command=gui)
dropdown.add_command(label="SAVE", command=mbox)
dropdown.add_command(label="OPEN")
dropdown.add_command(label="CLOSE", command=close)

dropdown2 = Menu()

dropdown2.add_command(label="UNDO")
dropdown2.add_command(label="REDO")
dropdown2.add_separator()
dropdown2.add_command(label="CUT")
dropdown2.add_command(label="COPY")
dropdown2.add_command(label="PASTE")

options.add_cascade(label="FILE", menu = dropdown)
options.add_cascade(label="EDIT", menu = dropdown2)
options.add_cascade(label="NAVIGATE")
options.add_cascade(label="CODE")
options.add_cascade(label="RUN")
options.add_cascade(label="TOOLS")
options.add_cascade(label="HELP")

root.config(menu = options)

root.mainloop()
# mywin.mainloop()