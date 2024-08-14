from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degreese C")

window = Tk()

hotImage = PhotoImage(file='hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,          #orientation of scale
              font= ('Consolas',20),
              tickinterval=10,          #adds numeric indicator for value
            #   showvalue=0,              #hides current value
              troughcolor="#69EAFF",
              fg = '#FF1C00',
              bg='#111111'
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])        #sets current value of slider 

scale.pack()


coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()