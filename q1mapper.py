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
    businessDict = json.loads(jsonobject)
    if (businessDict['hours'] != None):
        if ('Satruday' in businessDict['hours']):
            category_list_str = str(businessDict['categories'])
            categories_list = [i.strip() for i in category_list_str.split(',')]
            for categories_item in categories_list:
                print('%s\t%s' % (categories_item, businessDict['business_id']))
        elif 'Sunday' in businessDict['hours']:
            category_list_str = str(businessDict['categories'])
            categories_list = [i.strip() for i in category_list_str.split(',')]
            for categories_item in categories_list:
                print('%s\t%s' % (categories_item, businessDict['business_id']))
        elif ('Sunday' and 'Saturday') in businessDict['hours']:
            category_list_str = str(businessDict['categories'])
            categories_list = [i.strip() for i in category_list_str.split(',')]
            for categories_item in categories_list:
                print('%s\t%s' % (categories_item, businessDict['business_id']))
 #or (('Sunday' and 'Saturday') in businessDict['hours'])
 # or ('Sunday' in businessDict['hours']) or (('Sunday' and 'Saturday') in businessDict['hours']):