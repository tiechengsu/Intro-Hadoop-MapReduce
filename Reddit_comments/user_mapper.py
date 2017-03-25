#!/usr/bin/env python

import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	reader.next()
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line) != 8:
			coninue
		_,author,body,_,ups,_,_,_ = line
		writer.writerow([author,ups,len(body.split(' '))])

if __name__ == '__main__':
	mapper()
