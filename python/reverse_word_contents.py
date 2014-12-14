# Purpose: reads in a string and reverses it (white-space delimited) 
# @return: String 
def sReverse(s):
	length = len(s)
	e = length
	b = 0
	newS = ""
	last = True;					#if last char was a space

	for i in range(length, 0, -1):
		if (s[i -1] != ' '):			#checks if not space
			if last:
				e = i			#decrements counter for substring position
			last = False
		else:
			if (last):			#if previous char was whitespace
				newS += ' '
				e = i
			else:				#previous char was not a whitespace
				b = i - 1
				newS += s[b:e]	 	#add contents of previous whitespace-delimited string
				last = True
	
	s = newS
