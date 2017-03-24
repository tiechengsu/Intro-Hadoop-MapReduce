#!/usr/bin/python

import sys
import csv

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	reader.next()
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line)==19:
			author_id = line[3]
			node_type = line[5]

			if node_type=='question':
				id = line[0]
				writer.writerow([id,author_id])
			else:
				parent_id = line[6]
				writer.writerow([parent_id,author_id])


if __name__ == '__main__':
	mapper()
