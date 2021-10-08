# function of os module

import os 
hello  = os.path.basename("baz/foo")   # it return the base name of the file 
print(hello)                           # this function give basically the path name from the given file
          
hello_1 = os.path.dirname("baz/foo")   # it basically give the directory name from the path given
print(hello_1)

hello_2 = os.path.isdir("/baz/foo")     #It specifies whether the path is absolute or not.                    
print(hello_2)                          # In Unix system absolute path means path begins with the slash(‘/’

hello_3 = os.path.isdir("C:\\Users")     # this function specify whether the path is existing directory or not
print(hello_3)

hello_4 = os.path.isfile("C:\\Users\foo.cs")   # this fuction specify whter this file exist or not
print(hello_4)

hello_5 = os.getcwd()                    # this give the current working directory
print(hello_5)


hello_6 = os.chdir("../..")      # this change the current working directory 
print(hello_6)


directory = "Nikhil"                                        # leaf directory
parent_dir = "D:/Pycharm projects/GeeksForGeeks/Authors"    # parent directory 
path = os.path.join(parent_dir, directory)
print(path)


hello_7 = os.listdir("C:\\")     # it give the list of directory and files in the list dictonary
print(hello_7)