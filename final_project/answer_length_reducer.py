#!/usr/bin/python

import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	old_id = None
	count = 0
	total_len = 0
	question_len = 0
	for line in reader:
		if len(line)!=3:
			continue
		id,node_type,length = line
		if node_type == 'A':
			if old_id:
				if count>0:
					writer.writerow([old_id,question_len,total_len/count])
				else:
					writer.writerow([old_id,question_len,0])
			old_id = line[0]
			total_len = 0
			question_len = length
			count = 0
		else:
			count+=1
			total_len += float(length)
	if old_id:
		if count>0:
			writer.writerow([old_id,question_len,total_len/count])
		else:
			writer.writerow([old_id,question_len,0])
		



if __name__ == '__main__':
	reducer()
