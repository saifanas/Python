# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.pack(side=BOTTOM)

Button(frame,text='W',font=("Consalas",25),width=3).pack(side=TOP)
Button(frame,text='A',font=("Consalas",25),width=3).pack(side=LEFT)
Button(frame,text='S',font=("Consalas",25),width=3).pack(side=LEFT)
Button(frame,text='D',font=("Consalas",25),width=3).pack(side=LEFT)


window.mainloop()