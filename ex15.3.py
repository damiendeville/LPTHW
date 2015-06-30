# Prints out the instruciton to the user with a prompt.
print "Type in your filename:"
filename = raw_input("> ")


# Captures the user's input and assigns it to the variable txt
txt = open(filename)

# Prints out the contents of the file specified by the user by calling the 
# function "read" on the variable "txt", which is assigned to the user's input
print "Here's your file %r:" % txt
print txt.read()

# Closes the file.  This is counter intuitive to me since we're closing the VAR
# txt, not filename - need to investiage this
txt.close()

# Same as above
print "Type the filename again:"
file_again = raw_input("> ")


txt_again = open(file_again)

print txt_again.read()
txt_again.close()