#!/usr/bin/env python
'''
Suppose you want to know how view counts correlate with score, but only for posts that have been answered. Write a MapReduce program that makes a new dataset with the view counts and the score only for posts with at least one answer. What's the highest score and how many views did that post have?

This doesn't actually need a reducer since you are just filtering and writing out the results. You can set the number of reducers to zero by including the option -D mapred.reduce.tasks=0. This makes it so no reducers run, and the output from the mapper is the final output.

$ hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -D mapred.reduce.tasks=0 -files view_count_mapper.py -input Posts.xml -output scores -mapper view_count_mapper.py 

'''
import sys
import xml.etree.ElementTree as ET

def mapper():
	for row in sys.stdin:
		row = row.strip()
		
		if not row.startswith('<row'):
			continue
		
		parser = ET.fromstring(row)
		AnswerCount = parser.get('AnswerCount')
		Score = parser.get('Score')
		ViewCount = parser.get('ViewCount')
			
		if AnswerCount:	
			print '{0}\t{1}'.format(Score,ViewCount)

		del parser

if __name__ == '__main__':
	mapper()	
