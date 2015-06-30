## Notes

This is a file for tracking mistakes I make and questions I have for additional research so that I can learn from them over time without getting bogged down in meantime.

----

#### Exercise 4

http://learnpythonthehardway.org/book/ex4.html

##### Study Drills

1. the use of 4.0 is arbitrary here because all math is with whole numbers. Changing it to 4 makes no difference in this program.
2. It's true that 4.0 is a floating point number
3. This file includes the comments
4. "=" is used for assignment, where as "==" is used for mathmatical equality.
5. Yes, I'm familiar with the underscore - it is used in place of spaces in 
unix_and_programing.

----

#### Exercise 5

http://learnpythonthehardway.org/book/ex5.html

##### Study Drills

1. Changed all variables that started with my_ by using search and replace
2. Added lines 20-24 which convert inches to centimeters and pounds to 
kilograms
3. See https://docs.python.org/2/library/stdtypes.html#string-formatting-operations

	Conversion	Meaning 
	-----------------------------------------------------------------------------------
		'd' 	Signed integer decimal. 	 
		'i' 	Signed integer decimal. 	 
		'o' 	Signed octal value. 
		'u'		Obsolete type - identical to 'd'
		'x'		Signed hexadecimal (lowercase). 
		'X' 	Signed hexadecimal (uppercase). 
		'e' 	Floating point exponential format (lowercase). 
		'E' 	Floating point exponential format (uppercase). 
		'f' 	Floating point decimal format. 
		'F' 	Floating point decimal format. 
		'g' 	Floating point format. Uses lowercase exponential format if 
				exponent is less than -4 or not less than precision, decimal 
				format otherwise. 	
		'G' 	Floating point format. Uses uppercase exponential format if 
				exponent is less than -4 or not less than precision, decimal 
				format otherwise. 	
		'c' 	Single character (accepts integer or single character string). 	 
		'r' 	String (converts any Python object using repr()). 
		's' 	String (converts any Python object using str()). 
		'%' 	No argument is converted, results in a '%' character in the 
				result. 

4. Modified lines 23 and 24 substituting %s and %r - noteably, %d throws an 
error because the variables are all strings, not integers.

----

#### Exercise 6

http://learnpythonthehardway.org/book/ex6.html

##### Study Drills

1. Comments are included in ex06.1.py
2. Lines 3, 16, 29, 33, and 44 have strings inside another string in ex06.1.py
3. The author said there were 4, but there are actually 5 places where strings are inside strings.
4. This is called concatonation.  Using the + sign with strings results in concationation rather than a mathematical expression.

----

#### Exercise 7

http://learnpythonthehardway.org/book/ex7.html

##### Study Drills

1. Added Comments to the code in ex07.1.py
2. I didn't make any mistakes this time.
3. I don't use paper, but I'll create a file called NOTES.md to track them.
4 & 5 These are good things to remember. When you go to the next exercise, look at the mistakes you have made and try not to make them in this new one. Remember that everyone makes mistakes. Programmers are like magicians who fool everyone into thinking they are perfect and never wrong, but it's all an act. They make mistakes all the time.

----

#### Exercise 8

http://learnpythonthehardway.org/book/ex8.html

##### Notes

When I fist wrote ex08.py I somehow ended up with a tab at the begining of each line.  Not sure how, but python wouldn't execte it because it was an indentation error.

	File "/Users/damien/GitHub/LPTHW/ex9.0.py", line 6
    print "Hear are the days: ", days
    ^
	IndentationError: unexpected indent

This problem was either a bad indent on the first line, which the editor repeated, or 
a artifact from a previous editing session.

All initial statements lines need to start with no spaces (indentation comes later.)

##### Study Drills

1. No errors.
2. %r is used for a string and converts any python object using repr().  This means that Python returns a string containign a printable representation of an object https://docs.python.org/2/library/functions.html#func-repr.  Essentially, python will print the strings in the most efficient manner it can, not necessarilly as you wrote them.  %r is often used for debugging.  If you change it to %s Then no quotes are printed around any of the strings and the output looks like this:

Output 

	1 2 3 4
	one two three four
	True False False True
	%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s
	I had this thing. That you could type up right. But it didn't sing. So I said goodnight.

----

#### Exercise 9

http://learnpythonthehardway.org/book/ex9.html

##### Study Drills
1. No mistakes made.  
2. Went though and commented code in ex9.0.py 

----

#### Exercise 10

http://learnpythonthehardway.org/book/ex10.html

##### Notes

It seems that you can't use an escape character alone at the beginning of a format string

This works:

	print "%s a %s at the beginning of a line and add the word %s in the sentence with a format string" % ("\tAdd", "tab", "tab")
	
This Doesn't:

	print "%s Add a %s at the beginning of a line and add the word %s in the sentence with a format string" % ("\t", "tab", "tab")

Need to investigate why this is the case.

##### Study Drills

1. Memorize the escape sequences.  How about I just keep them handy.  I'm sure I'll learn them over time.  They're not that different from shell escapes any way.

	Escape 		What it does
	-------------------------------------------------------------------------
		\\ 			Backslash ()
		\' 			Single-quote (')
		\" 			Double-quote (")
		\a 			ASCII bell (BEL)
		\b 			ASCII backspace (BS)
		\f 			ASCII formfeed (FF)
		\n 			ASCII linefeed (LF)
		\N{name} 	Character named name in the Unicode database (Unicode only)
		\r ASCII 	Carriage Return (CR)
		\t ASCII 	Horizontal Tab (TAB)
		\uxxxx 		Character with 16-bit hex value xxxx (Unicode only)
		\Uxxxxxxxx 	Character with 32-bit hex value xxxxxxxx (Unicode only)
		\v 			ASCII vertical tab (VT)
		\ooo 		Character with octal value ooo
		\xhh 		Character with hex value hh


2 - 4. Played around with code as follows - also included in ex10.0.py

Code from ex10.0.py 

	fat_cat2 = '''
	I'll do a list:
	\t* Cat food
	\t* Fishies
	\t* Catnip\n\t* Grass
	'''
	
	print fat_cat2
	
	print "This is how to add a %s with a format string" % "\nnewline"
	print "This is how to add a %s with a format string" % "\ttab"
	
	print """%s a %s at the beginning of a line and add the word %s in the sentence 
		with a format string" % ("\tAdd", "tab", "tab")
		"""
	print "%s with a format strings and variables %s" % ("\nAgain", "\n")
	beginning = "%s a %s at the beggining of a line and add the word" % (
		"\tAdd", "tab")
	end = "%s in the sentence with a format string." % "tab" 
	
	print beginning, end

----

#### Exercise 11

http://learnpythonthehardway.org/book/ex11.html

##### Study Drills

1. raw\_input() takes input from the user.  Optionally, you can specify a prompt raw\_input('--->') prints '--->' as a prompt to the user. See:  https://docs.python.org/2/library/functions.html#raw_input

2. Here is another version of the above program with diffent prompts.  

Also It uses %s instead of %r so that it prints pretty.

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
	
3. Here is a new form, similar to the first one, asking different questions.

Aditional Code

	print "\n"
	print "How many beers have you had?",
	beers = raw_input()
	print "Would you like another?",
	answer = raw_input()
	
	print "\n"
	print "So, you've had %s beers and you said \'%s\' to another." % (
		beers, answer)
	print "\n"

4. In the original code we used %r which is the repr() format string in python it prints out the strings the way python sees them - i.e. with quotes and since the single quote character is used as short hand for "feet" it would look to python as the end of the string so it needs to be escaped. This is fixed in the second set of code which uses the format string %s

----

#### Exercise 12

http://learnpythonthehardway.org/book/ex12.html

##### Study Drills

1. Katahdin:LPTHW damien$ pydoc raw_input

output

	Help on built-in function raw_input in module __builtin__:
	
	raw_input(...)
	    raw_input([prompt]) -> string
	
	    Read a string from standard input.  The trailing newline is stripped.
	    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
	    On Unix, GNU readline is used if enabled.  The prompt string, if given,
	    is printed without a trailing newline before reading.
	(END)

2. Yup, typing q quits pydoc, who'd have thunk it.  

3. pydoc - Document generation and online help manual See:  https://docs.python.org/2/library/pydoc.html Got to say that pydoc is pretty cool

----

#### Exercise 13

http://learnpythonthehardway.org/book/ex13.html

##### Study Drills

1. The error comes from the fact that the argument is expecting more values on the command line than it got.
2. Here's the script

ex13.1.py

	from sys import argv
	
	script, first, second = argv
	
	print "The script is called:", script
	print "Your first variable is:", first
	print "Your second variable is:", second

3. This script combines raw_input() with argv

ex13.2.py

	# Study Drill 2
	from sys import argv
	
	script, beer, wheat, ipa, porter, stout = argv
	
	print "There are several kinds of", beer
	print "Some people like", wheat
	print "Others are fans of", ipa
	print "Still others like", porter
	print "I am partial to", stout

----

#### Exercise 14

http://learnpythonthehardway.org/book/ex14.html'

##### Study Drills

1. Zork and Adventure were early text based games.  You can play Zork at http://www.web-adventures.org/cgi-bin/webfrotz?s=ZorkDungeon 
2. Changed the prompt from "> " to "# "
3. Not sure what's so difficult to understand about using """ for multi-line statements with format strings, but, okay, I get it.
