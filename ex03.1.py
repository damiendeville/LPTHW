# This revision of ex3.py adds floating point numbers to the program
# This prints a sentence

print "I will now count my chickens:"

# This prints the word "Hens" and then adds 5 to 25 because division is first
# in the order of operations

print "Hens", 25.0 + 30.0 / 6.0

# This prints the word Roosters, and then calculates 25 * 3 and divides
# the answer 75 by 4 resulting in 3 (the remainder is dropped because we're not
# using floating point nubmers) and finally subtracts 3 from 100 resulting in
# 97

print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

# This prints "Now I will count the eggs"

print "Now I will count the eggs:"

# This calculates the number of eggs following the order of operations (PEMDAS)
# and retuns the number 7

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
print "Wait, what? How did a Hen lay 3/4 of an egg?"

# This prints the question "Is it true that 3 + 2 < 5 - 7?"

print "Is it ture that 3.0 + 2.0 < 5.0 - 7.0?"

# This actually evaluates the equation 3 + 2 < 5 - 7 and returns either "True"
# or "False" - "False" in this case since 5 is not less than -2

print 3.0 + 2.0 < 5.0 - 7.0

# These two statements print a questiion and calculates the result being asked
# in the quesion.

print "What is 3.0 + 2.0?", 3.0 + 2.0
print "What is 5.0 - 7.0?", 5.0 - 7.0

# This prints a sentence acknowloging why the question printed in line 28 is
# "False"
print "Oh, that's why it's False."

# This asks a quesiton, but doesn't have a question mark at the end of the
# sentence

print "How about some more."

# These ask quesitons and evalute the answers.  The first evaluates to "True"
# because 5 is greater than -2.  The second evaluates to "True" also because 5
# is greater than or equal to -2.  The third evlauates to "False" because 5 is
# NOT less than or equal to -2.

print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0
