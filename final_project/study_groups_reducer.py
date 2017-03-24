#!/usr/bin/python

import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	authors = []
	old_id = None
	for line in reader:
		if len(line)!=2:
			continue
		id,author_id = line
		if old_id and id!=old_id:
			writer.writerow([id,authors])
			authors = []
		old_id = id
		authors.append(author_id)
	if old_id:
		writer.writerow([id,authors])
			 
	


if __name__ == '__main__':
	reducer()
