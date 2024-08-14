from tkinter import *
from tkinter import colorchooser        #Submodule

def click():
    color = colorchooser.askcolor()
    colorHex = color [1]
    window.config(bg=colorHex)          #This will cahnge bacjground color
    
window =Tk()
window.geometry("420x420")
button = Button(text='click me',command=click)
button.pack()
window.mainloop()