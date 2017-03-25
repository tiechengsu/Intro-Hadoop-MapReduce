#!/usr/bin/env python

import sys
import csv

def reducer():
	old_author = None
	count_comments,count_upvotes,count_length = 0,0,0
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line)!=3:
			continue
		author,ups,body = line
		if old_author and old_author!=author:
			if count_comments!=0:
				writer.writerow([author,count_comments,count_upvotes/count_comments,count_length/count_comments])
			else:
				writer.writerow(author,0,0,0)

			count_comments,count_upvotes,count_length = 0,0,0
		old_author = author
		count_comments+=1
		count_upvotes+=int(ups)
		count_length+=int(body)
	if old_author:
		if count_comments!=0:
			writer.writerow([author,count_comments,count_upvotes/count_comments,count_length/count_comments])
		else:
			writer.writerow(author,0,0,0)

if __name__ == '__main__':
	reducer()
