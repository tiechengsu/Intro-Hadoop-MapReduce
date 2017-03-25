#!/usr/bin/env python
import sys
import csv


def reducer():
	reader = csv.reader(sys.stdin,delimiter='\t')
	love_count = 0
	hate_count = 0
	old_sub = None
	for line in reader:
		if len(line)!=3:
			continue
		subreddit,love,hate = line
		if old_sub and subreddit!=old_sub:
			print '{0}\t{1}'.format(old_sub,float(love_count-hate_count)/(love_count+hate_count))
		love_count += int(love)
		hate_count += int(hate)
		old_sub = subreddit
	if old_sub:
		print '{0}\t{1}'.format(old_sub,float(love_count-hate_count)/(love_count+hate_count))


if __name__ == '__main__':
	reducer()
