#!/usr/local/bin/python3.9
import sys


current_category = None
idlist = []
category = None 


for line in sys.stdin:
    line = line.strip()
    category, bid = line.split('\t')

    if current_category == category:
        idlist.append(bid)
    else:
        if current_category:
            print(current_category + '\t' + str(idlist))
            idlist.clear()
            idlist.append(bid)
            current_category = category
        idlist.append(bid)
        current_category = category
        
if current_category == category:
    print(current_category + '\t' + str(idlist))