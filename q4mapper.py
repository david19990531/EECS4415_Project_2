#!/usr/local/bin/python3.9

import sys
import json

for jsonobject in sys.stdin:
    bid = '-1'
    datetime = '-1'
    businessname = '-1'
    bcDict = json.loads(jsonobject)
    #it read the yelp_academic_dataset_checkin.json
    if (len(bcDict)) == 2:
        bid = bcDict['business_id']
        datetime = bcDict['date']
    else:
        bid = bcDict['business_id']
        businessname = bcDict['name']
    
    print(bid + "???" + datetime + "???" + businessname)
    