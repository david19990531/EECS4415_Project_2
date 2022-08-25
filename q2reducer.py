#!/usr/local/bin/python3.9
import sys

current_month = None
count = 0
month = None 


for line in sys.stdin:
    line = line.strip()
    month, counts = line.split('\t')

    if current_month == month:
        count = count + int(counts)
    else:
        if current_month:
            print('%s\t%s' % (current_month, str(round((count / 2189457) * 100, 2))) + '%')
        count = int(counts)
        current_month = month
        
if current_month == month:
    print('%s\t%s' % (current_month, str(round((count / 2189457) * 100, 2))) + '%')
