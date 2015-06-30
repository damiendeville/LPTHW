filename = raw_input("Type in the name of your file: ")
txt = open(filename)

print "Here is the contents of your file: \n"
print txt.read()