# nested loop = "The inner loop" will finish all of its itertations before
#                finsishing one iteration of the "outer loop"


rows = int(input("How may rows? "))
coloumns = int(input("How may coloumns? "))   
symbol = (input("Enter a symbol to use: "))


for i in range(rows):
    for j in range(coloumns):
        print(symbol, end="")
    print()  