#!/usr/bin/env python

import sys
import csv
from datetime import datetime

def mapper():
	reader = csv.reader(sys.stdin,delimiter='\t')
	writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
	for line in reader:
		if len(line)!=8:
			continue
		subreddit,_,body,create_utc,_,_,_,_ = line;
		dt = datetime.utcfromtimestamp(float(create_utc))
		date = dt.strftime('%Y_%m-%d')

		#if subreddit!='nfl':
			#continue
		if ('money' in body.lower()) or (('kid') in body.lower()):
			print date

if __name__ == "__main__":
	mapper()

			
