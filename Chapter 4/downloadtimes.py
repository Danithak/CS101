#!/usr/bin/python
# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(n):
    h=int(n/3600)
    m=int((n%3600)/60)
    s=n-(h*3600+m*60)
    hour='hour'
    minute='minute'
    second='second'
    if h!=1:
        hour='hours'
    if m!=1:
        minute='minutes'
    if s!=1:
        second='seconds'
    return str(h)+' '+hour+', '+str(m)+' '+minute+', '+str(s)+' '+second

def download_time(f,f_un,bw,bw_un):
    un_list=['b','kb','kB','Mb','MB','Gb','GB','Tb','TB']
    un_size=[1,2**10,2**10*8,2**20,2**20*8,2**30,2**30*8,2**40,2**40*8]
    for e in un_list:
        if f_un==e:
            f=f*un_size[un_list.index(e)]
        if bw_un==e:
            bw=bw*un_size[un_list.index(e)]
    return convert_seconds((f+0.0)/bw)



print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable




