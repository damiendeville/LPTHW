# import argument variable from module sys
from sys import argv

# import function exists from function path in module os
# this checks to see if the file exists or not
from os.path import exists

# declare argument values
script, from_file, to_file = argv

# print out what we're goint to do
print "Copying from %s to %s" % (from_file, to_file)

# In one line
indata = open(from_file).read()

# open output file for writing
out_file = open(to_file, 'w')

# write the contents of variable 'indata' to output file
out_file.write(indata)

# close both input and output files
# out_file.close()
# in_file.close()