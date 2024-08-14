import os
import shutil

path = "folder"

try:
    # os.remove(path)           # delete a file
    # os.rmdir(path)            # delete a empty directory
    shutil.rmtree(path)         # delete a directory containing
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have a permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")