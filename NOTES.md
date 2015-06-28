## Notes
----------

This is a file for tracking mistakes I make and questions I have for additional research so that I can learn from them over time without getting bogged down in meantime.

#### Exercise 8
----------

When I fist wrote ex08.py I somehow ended up with a tab at the begining of each line.  Not sure how, but python wouldn't execte it because it was an indentation error.

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

This worksf:

	print "%s a %s at the beginning of a line and add the word %s in the sentence with a format string" % ("\tAdd", "tab", "tab")
	
This Doesn't:

	print "%s Add a %s at the beginning of a line and add the word %s in the sentence with a format string" % ("\t", "tab", "tab")

Need to investigate why this is the case.