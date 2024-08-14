from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = PhotoImage(file='space3.png')
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photoimage = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0,0,image=photoimage,anchor=NW)

image_width = photoimage.width()
image_height = photoimage.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>= (WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>= (HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)
     
window.mainloop()