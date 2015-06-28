# Assigns "%r %r %r %r" to formatter
# %r is used for a string and converts any python object using repr()
# This means that Python returns a string containign a printable representation 
# of an object https://docs.python.org/2/library/functions.html#func-repr
# Essentially, python will print the strings in the most efficient manner it 
# can, not necessarilly as you wrote them.  %r is often used for debugging.  If 
# you change it to %s Then no quotes are printed around any of the strings and 
# the output looks like this:
#
# 1 2 3 4
# one two three four
# True False False True
# %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s
# I had this thing. That you could type up right. But it didn't sing. So I said 
# goodnight.

formatter = "%r %r %r %r"

# prints 1 2 3 4 (no quotes becasue these are integers?)

print formatter % (1, 2, 3, 4)

# prints 'one' 'two' 'three' 'four' 

print formatter % ("one", "two", "three", "four")

# prints True False False True
# No quotes are necessary and none are printed because True and False are 
# keywords representing the concept of true or false - i.e. the state of being 
# True or False

print formatter % (True, False, False, True)

# prints the string '%r %r %r %r' four times as below
# '%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
# This is becasue the variable "formatter" (%r %r %r %r) is used as the 
# conversion 4 times

print formatter % (formatter, formatter, formatter, formatter)

# prints the following line, all on one line
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 
# 'So I said goodnight.'if there were no commas in this, then it won't parse 
# correctly because the variable formatter calls
# for four arugments and the commas seperate arguments.

print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)