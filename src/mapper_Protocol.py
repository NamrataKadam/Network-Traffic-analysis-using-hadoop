#!/usr/bin/env python

import sys
p=0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	#print words 
	try:
		protocol_no=words[words.index(word)+2]
		if word=="Protocol" and protocol_no=="6":  
			
			print '%s\t%s' % ("TCP" , 1)
		if word=="Protocol" and protocol_no=="17":  
			
			print '%s\t%s' % ("UDP" , 1)
		if word=="Protocol" and protocol_no=="1":  
			
			print '%s\t%s' % ("ICMP" , 1)
	except:
		p+1
