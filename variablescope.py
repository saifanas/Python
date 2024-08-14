# scope = The region that a variable is recognized  
#         A variable is only available from inside the regionit is created.
#         A global and locally scoped versions of a variable can be created

name ="Bro"         # global scope(available inside & outside fuinctions)

def display_name():
    name = "Code"       # local scope (available only inside this function)
    print(name)
    
display_name()
print(name)