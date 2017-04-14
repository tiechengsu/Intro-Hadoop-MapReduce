#!/usr/bin/env python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin,delimiter='\t')
    writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    counts = [0]*14
    for line in reader:
        for i,c in enumerate(line):
            counts[i] += int(c)
    writer.writerow(counts)


if __name__ == '__main__':
    reducer()
