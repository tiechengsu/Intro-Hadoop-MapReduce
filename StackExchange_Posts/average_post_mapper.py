#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def mapper():
	for row in sys.stdin:
		row = row.strip()
		if not row.startswith('<row'):
			continue
		
		parser = ET.fromstring(row)

		first = parser.get('CreationDate')
		last = parser.get('LastActivityDate')
		
		first_dt = datetime.strptime(first, '%Y-%m-%dT%X.%f')
		last_dt = datetime.strptime(last, '%Y-%m-%dT%X.%f')
		
		dt = last_dt-first_dt
		print dt.days

		del parser

if __name__ == '__main__':
	mapper()
