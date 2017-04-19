#!/usr/bin/env python

import sys
import csv
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin,delimiter='\t')
    for line in reader:
        if len(line)!=8:
            continue
        subreddit = line[0]
        create_utc = line[3]
        dt = datetime.utcfromtimestamp(float(create_utc))
        date = int(dt.strftime('%d'))
        week = 3
        if date <= 7:
            week = 0
        elif date <= 14:
            week = 1
        elif date <= 21:
            week = 2
        print '{0}\t{1}'.format(subreddit,week)

if __name__ == '__main__':
        mapper()