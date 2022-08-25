#!/usr/local/bin/python3.9

import sys
import json

for jsonobject in sys.stdin:
    reviewdict = json.loads(jsonobject)
    newdate = reviewdict['date'].replace('-', '')
    newdate = newdate.replace(':', '')
    newdate = newdate.replace('-', '')
    if reviewdict['review_id'] != None:
        print('%s\t%s\t%s' % (reviewdict['review_id'], str(reviewdict['useful']), newdate))
        print('%s\t%s\t%s' % (reviewdict['review_id'], str(reviewdict['funny']), newdate))
        print('%s\t%s\t%s' % (reviewdict['review_id'], str(reviewdict['cool']), newdate))
        