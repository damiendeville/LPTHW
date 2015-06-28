name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

height_in_centimeters = height * 2.54 
weight_in_kilograms = weight * 0.453592 

print "%r is %r inches tall or %r centimeters tall." % (
	name, height, height_in_centimeters)
print "%r weighs %r pounds or %r kilograms." % (
	name, weight, weight_in_kilograms)


# Study Drills
# ------------
# 1. Changed all variables that started with my_ by using search and replace
# 2. Added lines 20-24 which convert inches to centimeters and pounds to 
# kilograms
# 3. See 
# https://docs.python.org/2/library/stdtypes.html#string-formatting-operations
#
# Conversion	Meaning 
# ------------------------------------------------------------------------------------
# 		'd' 	Signed integer decimal. 	 
# 		'i' 	Signed integer decimal. 	 
# 		'o' 	Signed octal value. 
#		'u'		Obsolete type - identical to 'd'
# 		'x'		Signed hexadecimal (lowercase). 
# 		'X' 	Signed hexadecimal (uppercase). 
# 		'e' 	Floating point exponential format (lowercase). 
# 		'E' 	Floating point exponential format (uppercase). 
# 		'f' 	Floating point decimal format. 
# 		'F' 	Floating point decimal format. 
# 		'g' 	Floating point format. Uses lowercase exponential format if 
# 				exponent is less than -4 or not less than precision, decimal 
#				format otherwise. 	
# 		'G' 	Floating point format. Uses uppercase exponential format if 
# 				exponent is less than -4 or not less than precision, decimal 
#				format otherwise. 	
# 		'c' 	Single character (accepts integer or single character string). 	 
# 		'r' 	String (converts any Python object using repr()). 
# 		's' 	String (converts any Python object using str()). 
# 		'%' 	No argument is converted, results in a '%' character in the 
#				result. 	 
# 4. Modified lines 23 and 24 substituting %s and %r - noteably, %d throws an 
# error because the variables are all strings, not integers.
