from tkinter import *

window = Tk()           # instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code")
window.config(background="lightgrey")

icon =PhotoImage(file='logo.png')
window.iconphoto(True,icon)

window.mainloop()       #place window on computer screen.listen for events