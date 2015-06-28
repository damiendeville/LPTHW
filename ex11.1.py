print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "\n"
print "So, you are %r old, %r tall and %r heavy." % (
	age, height, weight)

# Study Drills
# ------------
# 1. raw_input() takes input from the user.  Optionally, you can specify a 
# prompt raw_input('--->') prints '--->' as a prompt to the user.
# See:  https://docs.python.org/2/library/functions.html#raw_input
#
# 2. Here is another version of the above program with diffent prompts.  Also
# It uses %s instead of %r so that it prints pretty.

print "\n"
print "How old are you?"
age_yrs = raw_input('Enter your age in years: ')
print "How tall are you?"
height_ft_in = raw_input('Enter your height in feet and inches: ')
print "How much do you weigh?"
weight_lbs = raw_input('Enter your weight in pounds: ')
print "\n"
print "So, you are %s old, %s tall and %s heavy." % (
	age_yrs, height_ft_in, weight_lbs)

# 3. Here is a new form, similar to the first one, asking different questions.
print "\n"
print "How many beers have you had?",
beers = raw_input()
print "Would you like another?",
answer = raw_input()

print "\n"
print "So, you've had %s beers and you said \'%s\' to another." % (
	beers, answer)
print "\n"
# 4. In the original code we used %r which is the repr() format string in 
# python it prints out the strings the way python sees them - i.e. with quotes 
# and since the single quote character is used as short hand for "feet" it 
# would look to python as the end of the string so it needs to be escaped.  
# This is fixed in the second set of code which uses the format string %s