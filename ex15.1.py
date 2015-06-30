# Import "argv" (argument variable) from the module "sys"

from sys import argv

# Assign variables to the argument variable (script is the name of the python
# script and filename is the name of a file we want to open "ex15_sample.txt")

script, filename = argv

# Assigns the function open on of the variable filename to the variable txt

txt = open(filename)

# Prints out "Here is your file ex15_sample.txt" (or whatever file you call as 
# an argument to the python script)

print "Here's your file %r:" % filename

# Calls the function "read" on the variable "txt" which has been assigned to
# the argument variable "filename" which is specified on the command line.

print txt.read()

# Prints out the request, "Type the file name again"

print "Type the filename again:"

# Captures the user's input and assigns it to the variable "file_again"
file_again = raw_input("> ")

# Assigns the function open on the variable "file_again" to the variable 
# "txt_again"

txt_again = open(file_again)

# Prints out the contents of the file by calling the fucntion "read" on the 
# variable "txt_again" which has been assigned the function open on the variable
# "file_again" which is the name of the file the user types when prompted in 
# line 29.

print txt_again.read()