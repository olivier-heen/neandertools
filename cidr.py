#!/usr/bin/python3
# ##############################################################v##############
'''
Convert a cidr network to an address interval.    And vice-versa.

Usage:
    cidr.py [-d <sep>] [-c | -i] [ITEM]

options:
    -d <sep>    One character interval separator.    [default: -]
    -c          Leave cidr as is.
    -i          Leave interval as is.

Example:
    cidr.py 192.168.0.4-192.168.0.12
    192.168.0.4/30
    192.168.0.8/30
    192.168.0.12/32

Remarks:
    Bad cidr are approximated to the closest interval.
    Consecutive intervals are not aggregated.
'''

from sys import stdin as stdi
import ipaddress
from docopt import docopt as args


# ##############################################################v##############
def conv(line):
    '''Main conversion function.'''
    try:                                                        # Interval?
        init, stop = line.split(SEPA)
        init = ipaddress.IPv4Address(init.strip())
        stop = ipaddress.IPv4Address(stop.strip())
        cidr = ipaddress.summarize_address_range(init, stop)
        if INTL_ASIS:
            return line
        return '\n'.join(str(addr) for addr in cidr)
    except ValueError:
        try:                                                    # CIDR?
            cidr = ipaddress.ip_network(line, strict=False)
            init = str(cidr[0])
            stop = str(cidr[-1])
            if CIDR_ASIS:
                return line
            return init + SEPA + stop
        except (ValueError, TypeError):                         # Unknown
            return line


# ##############################################################v##############
if __name__ == "__main__":
    ARGS = args(__doc__)
    ITEM = ARGS['ITEM']
    CIDR_ASIS = ARGS['-c']
    INTL_ASIS = ARGS['-i']
    SEPA = ARGS['-d']
    if len(SEPA) > 1:
        quit('cidr.py: the interval delimiter must be a single character.')
    if SEPA in '.1234567890':
        quit('cidr.py: the interval delimiter cannot be a dot or a digit.')

    if ITEM:
        print(conv(ITEM))
    else:
        for LINE in stdi:
            print(conv(LINE.strip()))

# ##############################################################v##############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64     79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny note
# ##############################################################^##############
# NICE
#    --nmap     enable nmap shortened notation (192.168.0.5-37).
#    --strict   force strict mode evaluaton of CIDR.
