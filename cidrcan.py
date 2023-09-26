#!/usr/bin/python3
# ##############################################################v##############
'''
Find the smallest CIDR range containing an IPv4 address interval.

Usage:
    cidrcan.py MINI MAXI

Examples:
    cidrcan.py 192.168.1.71 192.168.1.99    # Expect 192.168.1.64/26
    cidrcan.py 172.16.4.1 172.23.20.255     # Expect 172.16.0.0/13
    cidrcan.py 127.255.255.255 128.0.0.0    # Expect 0.0.0.0/0
'''
# ##############################################################v##############

from ipaddress import summarize_address_range as cidr           # To CIDR
from ipaddress import ip_address as iton                        # IP to Number
from ipaddress import IPv4Address as ntoi                       # Number to IP
from docopt import docopt as args                               # Command line


def cidrcan(mini, maxi):
    '''Return the smallest CIDR range that encolses mini and maxi.'''
    if mini > maxi:                                             # Swap
        return cidrcan(maxi, mini)
    init, stop = 0, 2**32-1
    while init < stop:                                          # Derecursived
        half = (init + stop + 1) // 2
        if maxi < half:                                         # Go lower half
            stop = half - 1
        elif mini >= half:                                      # Go upper halt
            init = half
        else:                                                   # Split no more
            break
    return cidr(ntoi(init), ntoi(stop))                         # break or /32


# ##############################################################v###############
if __name__ == '__main__':
    ARGS = args(__doc__)

    try:
        MINI = int(iton(ARGS['MINI']))
        MAXI = int(iton(ARGS['MAXI']))
        print(next(cidrcan(MINI, MAXI)))                        # next for 1st

    except (ValueError, TypeError):
        print('MINI and MAXI must be IPv4 addresses in dot notation.')


# ##############################################################v##############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64     79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny note
# ##############################################################^##############
# MUST
#
#
# ##############################################################|##############
# NICE
#
# ##############################################################^##############
# Author:   Olivier Heen
# Date:     2023-09
# Comment:  Computing CIDR ranges from the top of my head is always difficult.
#           Like you have IP addresses all between 10.0.3.1 all 10.0.5.12, and
#           you want to find in which common CIDR range they fall: 10.0.0.0/21.
#           Now we can compute this with: cidrcan.py 192.168.1.19 192.168.1.71
