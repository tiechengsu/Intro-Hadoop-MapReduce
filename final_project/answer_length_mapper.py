#!/usr/bin/python
import sys
import csv

def mapper():
	
	reader = csv.reader(sys.stdin,delimiter='\t')
	reader.next()
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line)!=19:
			continue
		body = line[4]
		node_type = line[5]
		if node_type == "question":
			id = line[0]
			#'A' for question
			writer.writerow([id,'A',len(body)])
		elif node_type == "answer":
			parent_id = line[6]
			#'B' for answer
			writer.writerow([parent_id,'B',len(body)])


if __name__ == "__main__":
	mapper()
