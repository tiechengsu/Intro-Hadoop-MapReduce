#!/usr/bin/env python
import sys

def reducer():
	old_date = None
	mentions = 0
	for line in sys.stdin:
		date = line.strip();
		if old_date and old_date!=date:
			print("{}\t{}".format(old_date,mentions))
			mentions = 0
		old_date = date
		mentions+=1
	if old_date:
		print("{}\t{}".format(old_date,mentions))

if __name__ == "__main__":
	reducer()
