#!/usr/bin/python
# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

## This answer uses the date python library for simplification

from datetime import date

def daysBetweenDates(year1, month1, day1, year2, month2, day2):    
    d1 = date(year1, month1, day1)    
    d2 = date(year2, month2, day2)    
    dr = d2 - d1   
    return dr.days

# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases: 				## Loops through each test case to see if correct
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
