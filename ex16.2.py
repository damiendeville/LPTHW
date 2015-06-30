# Import arugment variable from module sys
from sys import argv

# assign names to argument variables
script, filename = argv

# print instructions using a format string to specify the file named on the 
# command line when running python ex16.0.py
print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

# capture the carriage return (^C wouldn't actually get captured, the shell 
# sends that to the python PID)
raw_input("?")

# print out opening the file.
print "Opening the file..."

# Open the file and assign it to the variable target -- upon which we'll operate
# two functions (truncate and write)
target = open(filename, 'w')

# Print truncating the file and then empty the contents to the bit bucket
# target.truncate() empties the file
print "Truncating the file.  Goodbye!"
target.truncate()

# Print some more instructions
print "Now I'm goint to ask you for three lines."

# capture three lines of text from the user and store them in 3 variables
# specify the promts via strings inside the parentheses
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Print another message to the user
print "I'm going to write these to the file."

# Write out the contents of the variables one at a time and add a newline in 
# between each one.  CLUNKY CODE
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

file = "%s \n%s \n%s \n" % (line1, line2, line3)
target.write(file)
#target.write(%r "\n" %r "\n" %r "\n") % (line1, line2, line3)

# print out a message to the user that the script is closing the file and 
# use the close operation on the variable target to close the file.
print "And finally, we close it."
target.close()