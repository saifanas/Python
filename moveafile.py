import os

source = "testfolder"

destination = "C:\\Users\\Saifa\\Desktop\\testfolder"


try:
    if os.path.exists(destination):
        print("There is a already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")