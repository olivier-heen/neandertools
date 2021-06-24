#!/usr/bin/python3

################################################################v###############
'''Convert successive numbers to intervals. And vice-versa.

Usage:
    tamp.py [options]

Options:
    -d <sep>    One character interval separator.    [default: -]

Examples:
    tamp.py < vlan.csv > addr.csv
    diff <(tamp.py test | tamp.py) sample  &&  echo "Involution."
'''
################################################################v###############

from sys    import stdin    as stdi
from docopt import docopt   as args

def show(init, stop):
    '''Print the interval "[init, stop]" or just "init" if bounds are equal.'''
    if init == stop:
        print(init)
    else:
        print(init, stop, sep=SEPA)

################################################################v###############
if __name__ == '__main__':
    INIT = CURR = NEXT = None
    INCL = lambda x, y: INCL(y, x) if x > y else range(x, y+1)  # Include bounds
    ARGS = args(__doc__)
    SEPA = ARGS['-d']
    if len(SEPA) > 1:
        quit('tamp.py: the interval delimiter must be a single character.')
    if SEPA in '.1234567890':
        quit('tamp.py: the interval delimiter cannot be a dot or a digit.')

    for l in stdi:
        line = l.strip()                                        # Line by line

        try:
            NEXT = int(line)                                    # It's an int?
            if INIT is None:                                    # Start interval
                INIT = CURR = NEXT
            elif NEXT == CURR+1:                                # Grow interval
                CURR = NEXT
            else:                                               # Stop interval
                show(INIT, CURR)                                # Show interval
                INIT = CURR = NEXT                              # Start another

        except ValueError:                                      # It's interval?

            if INIT is not None:                                # Ongoing list?
                show(INIT, CURR)                                # Show list
                INIT = CURR = NEXT = None                       # Stop list
            try:                                                # tamp interval?

                for step in INCL(*(int(i) for i in line.split(SEPA))):
                    print(step)
            except (ValueError, TypeError):                     # Can't tamp?
                print(line)                                     # Don't change

    if INIT is not None:                                        # Degenerate
        show(INIT, CURR)                                        # Just show

################################################################v###############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64      79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny notes
################################################################^###############
#MUST
#   --mini      Reduce the lists but do not expand the intervals.
#   --maxi      Expand the intervals but do not reduce the lists.
################################################################|###############
#NICE
#   Process negative numbers in intervals: -23--37  -37--23  11--13  -11-13.
################################################################^###############
