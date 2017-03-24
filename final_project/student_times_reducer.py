#!/usr/bin/python

import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	
	this_author_id = None
	counts = [0]*24
	for line in reader:
		if len(line)!=2:
			continue
		author_id,hour = line
		if this_author_id and this_author_id != author_id:
			write_record(author_id,counts,writer)
			counts = [0]*24
		this_author_id = author_id
		counts[int(hour)]+=1
	if this_author_id:
		write_record(author_id,counts,writer)

def write_record(author_id,counts,writer):
	max_hour = 0
	for i in range(24):
		max_hour = max(max_hour,counts[i])
	for i in range(24):
		if counts[i]==max_hour:
	  		writer.writerow([author_id,i])

if __name__ == "__main__":
	reducer()

	
	
