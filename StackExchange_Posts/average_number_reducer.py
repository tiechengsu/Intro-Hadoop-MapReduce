#!/usr/bin/env python
import sys


def reducer():
	oldTag = None
	tag_count = 0
	answer_count = 0
	for row in sys.stdin:
		data = row.strip().split('\t')
		if len(data)!=2:
			continue
		tag,count = data
		if oldTag and oldTag!=tag:
			print '{}\t{:.3f}'.format(oldTag,answer_count/tag_count)
			tag_count = 0
			answer_count = 0
		oldTag = tag
		tag_count += 1
		answer_count += int(count)
	if oldTag:
		print '{}\t{:.3f}'.format(oldTag,answer_count/tag_count)

if __name__ == '__main__':
	reducer()
