#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
reader.next() #skip the first line
for line in reader:
	if len(line)==19:
		author_id = line[3]
		added_at = line[8].strip()
		#added_at format 2012-02-21 05:08:03.824261+00
		hour = added_at[11:13]
		print "{0}\t{1}".format(author_id,hour)
	
