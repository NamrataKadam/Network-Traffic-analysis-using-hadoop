#!/usr/bin/env python

import sys
p=0
src_ip=[]
dest_ip=[]
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
		ip_addr=words[words.index(word)+3] 
		address=words[words.index(word)+1]
		if word=="Source" and address=="Address": 			
			src_ip.append(ip_addr)	
		if word=="Destination" and address=="Address": 
			dest_ip.append(ip_addr)
		
	except:
		p+1
for x,y in zip(src_ip,dest_ip):
	p=x+"->"+y
	print '%s\t%s' % (p , 1)
