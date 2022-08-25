#!/usr/local/bin/python3.9

import sys

current_review = None
ufccount = 0
review = None
time = None
review_dict = {}
review_dict_sort_top = {}

for line in sys.stdin:
    line = line.strip()
    review, counts, times = line.split('\t')
    
    if current_review == review:
        ufccount = ufccount + int(counts)
    else:
        if current_review:
            review_dict[current_review] = [ufccount, time]
            
        ufccount = int(counts)
        time = times
        current_review = review
        
if current_review == review:
    review_dict[current_review] = [ufccount, time]
    review_dict_sort = sorted(review_dict.items(), key = lambda x: x[1], reverse = True)
    
    for review_top_key, review_top_value in review_dict_sort[:4415]:
        print('%s\t%s' % (review_top_key, str(review_top_value[0])))
