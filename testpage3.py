#!/usr/bin/python

def proc(mylist):
    mylist = mylist + [6]
    return mylist

def proc2(mylist):
    mylist.append(6)
    return mylist

blah = [2, 3, 4, 5]

print proc(blah)
print proc2(blah)