#!/usr/bin/python
# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(x):
    p = 0 								## 1p stamp counter
    pp = 0 								## 2p stamp counter
    ppp = 0 							## 5p stamp counter
    if x < 5:							## Checks if x is less than 5 outright
        while 5 > x >= 2: 				## Condition necessary for 2p stamps
            x -= 2 						## Subtracts 2 from x for every 2p stamp needed
            pp += 1 					## Increases 2p stamp counter
            while x == 1: 				## Checks if there is a need for a 1p stamp
                x -= 1 					## Reduces x to 0
                p += 1 					## Increments 1p stamp counter 
                break 					## Terminates loop
    while x >= 5: 						## Loop that runs until x is below 5
        x -= 5 							## Decreases x for every 5p stamp
        ppp += 1 						## Increments for every 5p stamp
        while 5 > x >= 2: 				## Same code below for when x is less than 5
            x -= 2
            pp += 1
            while x == 1:
                x-=1
                p+= 1
                break
    return ppp, pp, p 					## Returns amount of 5p, 2p, and 1p stamps needed
        
    

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps
print stamps(50)
print stamps(3)
print stamps(4)