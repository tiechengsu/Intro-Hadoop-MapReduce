#!/usr/bin/env python

import sys

def reducer():
	post_count = 0
	lifetime_count = 0
	for row in sys.stdin:
		row = row.strip()
		if len(row)!=1:
			continue
		post_count += 1
		lifetime_count += int(row)

	print float(lifetime_count)/post_count



if __name__ == '__main__':
	reducer()
