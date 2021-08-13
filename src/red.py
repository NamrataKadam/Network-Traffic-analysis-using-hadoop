#!/usr/bin/env python
#reducer For Flow Analysis 
from operator import itemgetter
import sys
wordcount={}
total_entries=0

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    word, count = line.split('\t', 1)
    if word not in wordcount:
        wordcount[word] = 1
	total_entries+=1
    else:
        wordcount[word] += 1
	total_entries+=1

for dummy_word,dummy_count in wordcount.items():
    print dummy_word+"\t"+str(dummy_count)+"\t"
#print "Total Packets: "total_entries

    
