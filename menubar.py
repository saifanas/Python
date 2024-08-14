from tkinter import *

def openFile():
    print("File has been Opened")

def saveFile():
    print("File has been Saved")

def cut():
    print("You cut some text!")

def copy():
    print("You copy some text!")
    
def paste():
    print("You paste some text??")
window = Tk()

openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

cutImage = PhotoImage(file="cut.png")
copyImage = PhotoImage(file="copy.png")
pasteImage = PhotoImage(file="paste.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = Menu(window,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut,image=cutImage,compound='left')
editMenu.add_command(label="Copy",command=copy,image=copyImage,compound='left')
editMenu.add_command(label="Paste",command=paste,image=pasteImage,compound='left')


window.mainloop()