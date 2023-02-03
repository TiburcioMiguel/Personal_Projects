## This is intended to create a directory inside the current directory, and take all files of that
## directory, and move them to the newly created directory, and name the directory with the date that the 
## script is run
import os
import datetime
from datetime import date
import shutil
   
## This function will now create the directory
def create_directory():
    ## I will first get the current date so that I can name the directory 
    directory_name = date.today()
    parent_directory = os.getcwd()

    ## Join the name of the directory to the parent directory
    new_directory = os.path.join(parent_directory, str(directory_name))

    ## Now actually create the new direcotory
    os.mkdir(new_directory)

    ## Now iterate through the files in the parent directory to move them to the 
    ## new directory
    for file in os.listdir(parent_directory):
        if file == "Condense_Folder.py":
            continue
        shutil.move(file, new_directory)
    

create_directory()







    

    