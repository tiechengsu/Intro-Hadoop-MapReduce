#!/usr/bin/env python

import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	reader.next()
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line)!=8:
			continue
		subreddit = line[0]
		body = line[2]
		love,hate = 0,0
		if 'love' in body:
			love = 1
		if 'hate' in body:
			hate = 1
		writer.writerow([subreddit,love,hate])

if __name__=='__main__':
	mapper()



