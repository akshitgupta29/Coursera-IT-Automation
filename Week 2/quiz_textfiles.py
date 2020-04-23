'''
@author: Akshit Gupta
'''
# Link: https://www.coursera.org/learn/python-operating-system/quiz/1oBDy/practice-quiz-managing-files-directories/attempt?redirectToCover=true

import os
import datetime

#Question 1:
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open (filename, 'w') as file:
        file.write(comments)
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.py"))

#Question 2

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
    if not os.path.exists(directory):
        os.mkdir(directory)
  # Create the new file inside of the new directory
    os.chdir(directory)
    open(filename, 'w')
  # Return the list of files in the new directory
    return os.listdir()
print(new_directory("PythonPrograms", "script.py"))

# Question 4
def file_date(filename):
    # Create the file in the current directory
    open (filename, 'w')
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a readable format, then into a string
    date1 = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    # Return just the date portion 
    # Hint: how many characters are in “yyyy-mm-dd”? 
    return ("{0}".format(date1))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyy

