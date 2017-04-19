#!/usr/bin/env python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin,delimiter='\t')
    writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    oldSubreddit = None
    oldWeek = None
    count = 0
    for line in reader:
        subreddit,week = line
        if oldSubreddit and oldWeek and (subreddit!=oldSubreddit or oldWeek!=week):
            writer.writerow([oldSubreddit,oldWeek,count])
            count = 0
        oldSubreddit = subreddit
        oldWeek = week
        count+=1
    if subreddit:
        writer.writerow([subreddit,week,count])

if __name__ == '__main__':
    reducer()
