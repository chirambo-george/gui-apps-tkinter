# At this point app is only able to process integer data

from tkinter import *

def rect():
    l2 = l.get() 
    w2 = w.get()
    area = l2*w2
    result.insert(0, area)
    
    
root = Tk()
root.title("AREA OF A RECTANGLE")

l = IntVar()
w = IntVar()

Label(text="Length",font=("consolas", 14)).grid(row=0, column=0)
length = Entry(textvariable=l)
length.grid(row=0,column=1)

Label(text="Width",font=("consolas", 14)).grid(row=1, column=0)
width = Entry(textvariable=w)
width.grid(row=1,column=1)

Label(text="Area",font=("consolas", 14)).grid(row=2, column=0)
result = Entry()
result.grid(row=2,column=1)

btn = Button(text="Calculate", font=("consolas", 14), command=rect)
btn.grid(row=3, column=0)

root.mainloop()