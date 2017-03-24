#!/usr/bin/python

import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	reader.next()
	for line in reader:
		if len(line)!=19:
			continue
		node_type = line[5]
		if node_type == "question":
			tagnames = line[2]
			tags = tagnames.split()
			for tag in tags:
				print tag
				
		

if __name__ == '__main__':
	mapper()
