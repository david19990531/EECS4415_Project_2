#!/usr/local/bin/python3.9

import sys
import json


'''
 
    businessList = []
    #Because this data file has more than one json object, then put them into a list
    with open(args.fileName, encoding= "UTF-8") as f:
        for jsonObject in f:
            businessDict = json.loads(jsonObject)
            businessList.append(businessDict)
'''



for jsonobject in sys.stdin:
    userdict = json.loads(jsonobject)
    if (userdict['yelping_since'] != None):
        since_list_str = str(userdict['yelping_since'])
        since_list = [i.strip() for i in since_list_str.split('-')]
        if since_list[1] == '01':
            since_list[1] = '1'
        elif since_list[1] == '02':
            since_list[1] = '2'
        elif since_list[1] == '03':
            since_list[1] = '3'
        elif since_list[1] == '04':
            since_list[1] = '4'
        elif since_list[1] == '05':
            since_list[1] = '5'
        elif since_list[1] == '06':
            since_list[1] = '6'
        elif since_list[1] == '07':
            since_list[1] = '7'
        elif since_list[1] == '08':
            since_list[1] = '8'
        elif since_list[1] == '09':
            since_list[1] = '9'
        else:
            pass
        print('%s\t%s' % (since_list[1], '1'))
    
