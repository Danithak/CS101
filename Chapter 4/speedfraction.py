#!/usr/bin/python

# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.0 # km per second

def speed_fraction(trace, distance):
    x = (distance * 2.0 / trace) * 1000
    print x
    y = x / speed_of_light
    return y
    



print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?








