from tkinter import *
import tkinter as tk



counter = 0
def stop():
    root.destroy()

def digit_count(mylabel):
    counter = 0
    def digit():
        global counter
        counter += 1
        mylabel.config(text= str(counter))
        mylabel.after(1000, digit)
    digit()

root = tk.Tk()
root.title("DIGIT COUNTER")
root.geometry("500x500")
    
mylabel = Label(fg='red', font=50)
mylabel.pack()

digit_count(mylabel)

close = Button(text='Terminate', command = stop).pack()

root.mainloop()