# import argument variable from module sys
from sys import argv

# import function exists from function path in module os
# this checks to see if the file exists or not
from os.path import exists

# declare argument values
script, from_file, to_file = argv

# print out what we're goint to do
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# In one line
indata = open(from_file).read()

# print out the length of the input file
#print "The input file is %d bytes long" % len(indata)

# Check to see if the output file exists, and report status
print "Does the output file exist? %r" % exists(to_file)

# Print out instructions
print "Ready, hit RETURN to continue, CRTL-C to abort."

# Capture Carriage return
raw_input()

# open output file for writing
out_file = open(to_file, 'w')

# write the contents of variable 'indata' to output file
out_file.write(indata)

# Print out that we are done
print "Alright, all done."

# close both input and output files
out_file.close()
# in_file.close()