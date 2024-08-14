# radio buttons =  similar to checkbox, but you can only select one from group
from tkinter import *

food = ["pizza","hamburger","hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("you ordered a hamburger!")
    elif(x.get()==2):
        print("you ordered a hotdog!")
    else:
        print("huh?")
window = Tk()

pizzaImage = PhotoImage(file='pixxa.png')
hamburgerImage = PhotoImage(file='hamburger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],     #adds text to radio buttons
                              variable=x,           #groups radiobuttons together if they share the same variable
                              value=index,          #assigns each radiobuttons a different value
                              padx = 25,            #adds padding on x-axis              
                             font=("Impact",50),
                             image=foodImages[index],   #adds radiobuttons to images
                             compound='left',           #adds image & text  (left-side)
                             indicatoron=0,             #eliminate circle indicators
                             width = 375,               #sets width for radio buttons
                             command=order              #set command of radiobutton to function
                             )                 
    radiobutton.pack(anchor=W)

window.mainloop()