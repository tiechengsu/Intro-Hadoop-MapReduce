#!/usr/bin/env python

import sys
import csv

def mapper():
    characters = ['Tyrion','Daenerys','Jon','Arya','Sansa','Cersei','Joffrey','Petyr','Jaime','Bran','Sandor','Thron','Varys','Margaery']
    writer = csv.writer(sys.stdout,delimiter='\t',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    reader = csv.reader(sys.stdin,delimiter='\t')
    for line in reader:
        if len(line)!=8:
            continue
        count = [0]*len(characters)
        subreddit = line[0]
        body = line[2]

        if subreddit!='gameofthrones':
            continue
        for i,v in enumerate(characters):
            if v in body:
                count[i]+=1
        writer.writerow(count)

if __name__ == "__main__":
    mapper()
