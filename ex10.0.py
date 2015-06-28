tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape 		What it does
# -------------------------------------------------------------------------
#	\\ 			Backslash ()
#	\' 			Single-quote (')
#	\" 			Double-quote (")
#	\a 			ASCII bell (BEL)
#	\b 			ASCII backspace (BS)
#	\f 			ASCII formfeed (FF)
#	\n 			ASCII linefeed (LF)
#	\N{name} 	Character named name in the Unicode database (Unicode only)
#	\r ASCII 	Carriage Return (CR)
#	\t ASCII 	Horizontal Tab (TAB)
#	\uxxxx 		Character with 16-bit hex value xxxx (Unicode only)
#	\Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
#	\v 			ASCII vertical tab (VT)
#	\ooo 		Character with octal value ooo
#	\xhh 		Character with hex value hh

fat_cat2 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_cat2

print "This is how to add a %s with a format string" % "\nnewline"
print "This is how to add a %s with a format string" % "\ttab"

print "%s a %s at the beginning of a line and add the word %s in the sentence with a format string" % ("\tAdd", "tab", "tab")
print "%s with a format strings and variables %s" % ("\nAgain", "\n")
beginning = "%s a %s at the beggining of a line and add the word" % ("\tAdd", "tab")
end = "%s in the sentence with a format string." % "tab" 

print beginning, end

