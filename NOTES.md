## This is a file for tracking the kind of mistakes I make so that I can learn from them.

#### Exercise 8
----------

	File "/Users/damien/GitHub/LPTHW/ex9.0.py", line 6
    print "Hear are the days: ", days
    ^
	IndentationError: unexpected indent

This problem was either a bad indent on the first line, which the editor repeated, or 
a artifact from a previous editing session.

All initial statements lines need to start with no spaces (indentation comes later.)

#### Exercise 10
-----------

It seems that you can't use an escape character alone at the beginning of a format string

	This works
	print "%s a %s at the beginning of a line and add the word %s in the sentence with a format 	string" % ("\tAdd", "tab", "tab")
	
	This Doesn't
	print "%s Add a %s at the beginning of a line and add the word %s in the sentence with a format 	string" % ("\t", "tab", "tab")
