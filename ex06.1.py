# Assigns a string with a formatted variable %d = to 10 to the variable x

x = "There are %d types of people." % 10

# Assigns the value "binary" to the variable "binary" 

binary = "binary"

# Assigns the value "don't" to the variable "do_not"

do_not = "don't"

# Assigns the string "Those who know binary and those who don't" by using a formatted
# variable %s with the values of the variables defined above (binary & do_not)

y = "Those who %s and those who %s." % (binary, do_not)

# Print statement to print out the value of variable x

print x

# Print statement to print out the value of the variable y

print y

# Print out the string "I said: 'There are 10 types of people'.'" by substituting the 
# variable x for the formatted variable %r embedded in the string.

print "I said: %r." % x

# Print out the string "I also said: 'Those who know binary and those who don't.'." 
# by substituting the variable y for the formatted variable %s

print "I also said: '%s' ." % y

# Assign the value "False" to the variable "hilarious"

hilarious = False

# Assigns the value "Isn't that joke so funny?! %r" to the variable joke_evaluaiton
# This is tricky, because %r is not formatted in this line, it gets formatted below in 
# the print statement.  Took me a while to figure out where %r was being formatted.

joke_evaluation = "Isn't that joke so funny?! %r"

# prints out the variable "joke_evaluaiton" and provides the variable "hilarrious" as
# the format for %r contained in "joke_evaluation"

print joke_evaluation % hilarious

# Assigns the value "This is the left side of..." to w (which is short for west, which
# is on the left side of the compass).

w = "This is the left side of..."

# Assings the value "a string with a right side" to e (also a compass reference)

e = "a string with a right side."

# Prints out e + w concatonating the two together resulting in the sentence "This is 
# the left side of...a string with a right side."

print w + e



# Study Drill Answers
# -------------------
# 1. Comments above
# 2. Lines 3, 16, 29, 33, and 44 have strings inside another string
# 3. Yes, you lied, there are 5 places
# 4. This is called concatonation.  Using the + sign with strings results in concationation rather
# than a mathematical expression.

