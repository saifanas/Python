from tkinter import *

def create_window():
    new_window = Tk()            #Toplevel() new window 'on top' of other windows. linked to a 'bottom' window.   
                                 # Tk() = new independent window
    old_window.destroy()         # closed out of old window
                                 
old_window = Tk()

button = Button(old_window,text="create new window",command=create_window).pack()

old_window.mainloop()