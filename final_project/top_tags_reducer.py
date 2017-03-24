#!/usr/bin/python

import sys
import csv

def reducer():
	count = 0
	old_tag = None
	top10 = []
	for line in sys.stdin:
		tag = line.strip()
		if old_tag and old_tag!=tag:
			top10 = updateTop10(top10,old_tag,count)
			count = 0
		old_tag = tag
		count+=1
	if old_tag:
		top10 = updateTop10(top10,old_tag,count)
	for t,c in top10:
		print "{0}\t{1}".format(t,c)

def updateTop10(top10,tag,count):
	if len(top10)<10 or count > top10[9][1]:
		top10.append([tag,count])
		top10.sort(key=lambda t:t[1],reverse=True)
		top10 = top10[:10]
	return top10
		
if __name__ == "__main__":
	reducer()
