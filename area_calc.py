# At this point app is only able to process integer data

from tkinter import *

def calc():
    var2 = var1.get()
    var3 = 3.142*var2*var2
    area.insert(0, var3)
    
def clear():
    radius.delete(0, END)
    area.delete(0, END)
    
root = Tk()
root.title("CIRCLE AREA CALCULATOR")
root.geometry('500x500')

var1 = IntVar()
Label(text="Enter Radius: ").grid(row=0,column=0)
radius = Entry(textvariable=var1)
radius.grid(row=0, column=1)

Label(text="AREA: ").grid(row=1, column=0)
area = Entry()
area.grid(row=1, column=1)

btn = Button(text="CALCULATE", command=calc, width=20).grid(row=2, column=0)
btn2 = Button(text="CLEAR", command=clear, width=20).grid(row=2, column=1)

root.mainloop()
