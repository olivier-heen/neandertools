#!/usr/bin/python3

# ##############################################################v##############
'''Convert successive numbers to intervals. And vice-versa.

Usage:
    tamp.py [options]

Options:
    -d <sep>    One character interval delimiter.    [default: -]

Examples:
    tamp.py < vlan.csv > addr.csv
    diff <(tamp.py test | tamp.py) sample  &&  echo "Involution."
'''
# ##############################################################v##############

from sys import stdin as stdi
from docopt import docopt as args


def show_interval(init, stop):
    '''Print "init-stop" or just "init" if bounds are equal.'''
    if init == stop:
        print(init)
    else:
        print(init, stop, sep=SEPA)


def boom(val1, val2):
    '''Explode interval "val1-val2" as a number range.'''
    return boom(val2, val1) if val1 > val2 else range(val1, val2+1)


def conv():
    '''Main conversion loop.'''
    init = curr = look = None

    for read in stdi:
        line = read.strip()                                     # Line by line

        try:
            look = int(line)                                    # It's an int?
            if init is None:                                    # Start interv.
                init = curr = look
            elif look == curr+1:                                # Grow interv.
                curr = look
            else:                                               # Stop interv.
                show_interval(init, curr)                       # Show interv.
                init = curr = look                              # Start another

        except ValueError:                                      # Not an int

            if init is not None:                                # Must flush?
                show_interval(init, curr)
                init = curr = look = None
            try:                                                # Interval?
                val1, val2 = line.split(SEPA)
                for step in boom(int(val1), int(val2)):         # Explode
                    print(step)
            except (ValueError, TypeError):                     # Unknown
                print(line)                                     # Leab as is

    if init is not None:                                        # Degenerate
        show_interval(init, curr)                               # Just show


# ##############################################################v###############
if __name__ == '__main__':
    ARGS = args(__doc__)
    SEPA = ARGS['-d']
    if len(SEPA) > 1:
        quit('tamp.py: the interval delimiter must be a single character.')
    if SEPA in '.1234567890':
        quit('tamp.py: the interval delimiter cannot be a dot or a digit.')

    conv()

# ##############################################################v##############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64     79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny note
# ##############################################################^##############
# MUST
#   --mini      Reduce the lists but do not expand the intervals.
#   --maxi      Expand the intervals but do not reduce the lists.
# ##############################################################|##############
# NICE
#   Process negative numbers in intervals: -23--37  -37--23  11--13  -11-13.
# ##############################################################^##############
