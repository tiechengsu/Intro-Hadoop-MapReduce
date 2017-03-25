#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

def mapper():
	for row in sys.stdin:
		row = row.strip()
		if not row.startswith('<row'):
			continue
		parser = ET.fromstring(row)
		Tags = parser.get('Tags')
		AnswerCount = parser.get('AnswerCount')
		
		if Tags:
			Tags = Tags.replace('<',' ')
			Tags = Tags.replace('>',' ')
			Tags = Tags.split()
		if isinstance(Tags,list):
			for Tag in Tags:
				print '{0}\t{1}'.format(Tag,AnswerCount)

		elif Tags:
			print '{0}\t{1}'.format(Tags,AnswerCount)
if __name__ == '__main__':
	mapper()
