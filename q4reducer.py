#!/usr/local/bin/python3.9


import random
import string
import sys
#generate a random User Id, 26+26+9+2 = 63, 63^22, it is pretty pretty hard to have the same UserID
def generate_random_unique_string():
    stringlist = random.sample(string.digits + string.ascii_letters + '-' + '_', 22)
    randomstring = ''.join(stringlist)
    # if randomstring in userId:
    #     generate_random_unique_string()
    # else:
    #     userId.append(randomstring)
    return randomstring
# set the initial business_name, business_id and the tempoary datelist.
current_bname = None
current_bid = None
tmpdatelist = None
for line in sys.stdin:
    line = line.strip()
    bid, date, bname = line.split('???')
    # print('%s\t%s\t%s' % (bid, date, bname))
    #if it is same then it means, this is checkin business and print out with date
    if current_bid == bid:
        #bid -1 xxx
        if date == '-1':
            current_bname = bname
            current_bid = bid
        #bid 2022-02-02 -1
        if bname == '-1':
            current_bid = bid
            tmpdatelist = [i.strip() for i in date.split(',')]
    #if not, then check if it is the first one or it is not the checkin business
    else:
        if tmpdatelist:
            for eachdate in tmpdatelist:
                uid = generate_random_unique_string()
                #In this place, becuase the bid is different, then it should use current_bname
                print('%s\t%s\t%s' % (uid, eachdate, current_bname))
            tmpdatelist = None
        if date == '-1':
            current_bname = bname
            current_bid = bid
        if bname == '-1':
            current_bid = bid
            tmpdatelist = [i.strip() for i in date.split(',')]
if(current_bid == bid):
    #last line is the business name
    if date == '-1':
        for eachdate in tmpdatelist:
            uid = generate_random_unique_string()
            #In this place and this is the last line
            #It needs to check if it is data from business or checkin
            #if it show the business name, then just use bname
            print('%s\t%s\t%s' % (uid, eachdate, bname))
    else:
        #last line is the date
        tmpdatelist = [i.strip() for i in date.split(',')]
        for eachdate in tmpdatelist:
            uid = generate_random_unique_string()
            #In this place, the last line is the date information,
            #Then, it need to use the cuurent_bname
            print('%s\t%s\t%s' % (uid, eachdate, current_bname))
        
        