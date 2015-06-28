from sys import argv 

script, user_name = argv
print "Hi, %s, I'm the %s scritp" % (user_name, script)
print "I'm going to ask you a few questions about your lunch order."

soda_pref = raw_input("What kind of soda do you like? ")
sandwich_pref = raw_input("What kind of sandwich do you like? ")
chip_pref = raw_input("Would you like Chips? ")

print """
So %s you'd like a %s, 
A %s sandwich,
And you said %s to chips.
""" % (user_name, soda_pref, sandwich_pref, chip_pref)