#!/usr/bin/python3
# ##############################################################v###############
'''
Convert IPv4 to decimal. And vice-versa. Also works on intervals.

Usage:
    iton.py [options] [ITEM]

Options:
    -d <sep>    One character interval separator.    [default: -]
    --addr      Just convert decimal to addresse.
    --numb      Just convert addresse to decimal.

Example:
    iton.py 93.184.216.34
    1572395042
    diff <( iton.py hosts | iton.py ) hosts &&  echo "Involution"
'''

from sys import stdin as stdi
from ipaddress import ip_address as addr
from docopt import docopt as args


# ##############################################################v###############
def conv(line):
    '''Main conversion function.'''
    try:                                                        # Interval?
        item1, item2 = line.split('-')

        try:                                                    # IP interval?
            addr1, addr2 = addr(item1), addr(item2)
            numb1, numb2 = int(addr1), int(addr2)
            if ADDR:
                return str(addr1) + SEPA + str(addr2)
            return str(numb1) + SEPA + str(numb2)

        except ValueError:

            try:                                                # Decim. intrv?
                numb1, numb2 = int(item1), int(item2)
                addr1, addr2 = addr(numb1), addr(numb2)
                if NUMB:
                    return str(numb1) + SEPA + str(numb2)
                return str(addr1) + SEPA + str(addr2)

            except ValueError:                                  # None of above
                return line                                     # Leave as is

    except ValueError:                                          # Not interval

        try:                                                    # IPv4?
            addr0 = addr(line)
            numb0 = int(addr0)
            return str(addr0 if ADDR else numb0)

        except ValueError:                                      # Not IPv4

            try:                                                # Decimal?
                numb0 = int(line)
                addr0 = addr(numb0)
                return str(numb0 if NUMB else addr0)

            except ValueError:                                  # Not decimal
                return line                                     # Leave as is


# ##############################################################v##############
if __name__ == '__main__':
    ARGS = args(__doc__)
    ITEM = ARGS['ITEM']
    ADDR = ARGS['--addr']
    NUMB = ARGS['--numb']
    SEPA = ARGS['-d']
    if len(SEPA) > 1:
        quit('iton.py: the interval delimiter must be a single character.')
    if SEPA in '.1234567890':
        quit('iton.py: the interval delimiter cannot be a dot or a digit.')

    if ITEM:
        print(conv(ITEM))
    else:
        for LINE in stdi.readlines():
            print(conv(LINE.strip()))

# ##############################################################v##############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64     79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny note
# ##############################################################^##############
