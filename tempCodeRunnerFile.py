from tkinter import *

window = Tk()

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = PhotoImage(file='car2.png')
myimage = canvas.create_image()
window.mainloop()