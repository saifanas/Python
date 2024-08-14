from tkinter import *
from tkinter import messagebox          #import messagebox library

def click():
    # messagebox.showinfo(title='This is an info message box', message='you are a person')
    # messagebox.showwarning(title='Warning', message='You have a VIRUS!')
    #  messagebox.showerror(title='ERROR!!', message='something went wrong!! :(')
    
    # if messagebox.askretrycancel(title='ask of cancel',message='Do you want retry the thing'):
    #     print('You retried a thing!')
    # else:
    #     print('You canceled a thing! :(')
    
    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #     print('I like cake too :)')
    # else:
    #     print('Why do you not like cake?')
    
#    answer = messagebox.askquestion(title='ask question',message='Do you like pie??')
#    if(answer =='yes'):
#        print('I like pie too!!')
#    else:
#        print('Why do you not like piee?')
   
   answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?')
   if(answer==True):
       print("You like to code :(")
   elif(answer==False):
       print("Then why are you watching a video on coding?")
   else:
       print("You have dodge a question?")   
window = Tk()

button = Button(window,text='click me',command=click)
button.pack()


window.mainloop()