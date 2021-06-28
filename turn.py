#!/usr/bin/python3
# ##############################################################^##############
'''Turn a data table into its transpose or into vectors.

Usage:
    turn.py [-1 | -2 | -3 | -4] [<file>]

Options:
   -1       turn the table into a vector (first normal form).
   -2       transpose the table   (swap key and value roles).
   -3       turn the transpose into a vector    (-3 = -2 -1).
   -4       identity, just order and strip      (-4 = -2 -2).

Examples:
    turn.py -1 one-key-many-values > one-key-one-value
    diff <(turn.py -3 data) <(turn.py -2 data | turn.py -1) &&  echo "-3=-2-1"
    diff <(turn.py -4 data) <(turn.py -2 data | turn.py -2) &&  echo "-4=-2-2"
'''

# ##############################################################^##############
from docopt import docopt as args

SEPA = ',\t '                                                   # Separator
DATA = {}
ROTA = {}


def read(file):
    '''Read a data grid in a dictionary of sets.'''
    for line in file:
        if line.find(',') > 0:
            key, *val = [item.strip() for item in line.strip().split(',')]
            val = [v for v in val if v]
            if val != []:
                DATA.setdefault(key, set(val)).update(val)


def vect(data):
    '''Print one key and one value per line.'''
    for key in sorted(data):
        for val in sorted(data[key]):
            print(key, val, sep=SEPA)


def grid(data):
    '''Print one key and many values per line.'''
    for key in sorted(data):
        print(key, SEPA.join(data[key]), sep=SEPA)


# ##############################################################^##############
if __name__ == '__main__':
    ARGS = args(__doc__)

    if ARGS['<file>']:
        with open(ARGS['<file>']) as FILE:                      # From file
            read(FILE)
    else:                                                       # From stdin
        from sys import stdin as FILE
        read(FILE)

    if ARGS['-2'] or ARGS['-3']:                                # Rotate
        for KEY in DATA:
            for VAL in DATA[KEY]:
                if VAL in ROTA:
                    ROTA[VAL].update([KEY])
                else:
                    ROTA[VAL] = set([KEY])

    if ARGS['-1']:
        vect(DATA)
    if ARGS['-2']:
        grid(ROTA)
    if ARGS['-3']:
        vect(ROTA)
    if not (ARGS['-1'] or ARGS['-2'] or ARGS['-3']):
        grid(DATA)

# ##############################################################v##############
#   This code is meant to fit on 79 columns according to PEP 8. #<-64     79->#
#   I like to use the 64 first columns for code and the last 15 # for tiny note
# ##############################################################^##############
# MUST
#   Handle trail commas in CSV
#   Make sure that options -1 -2 -3 -4 are mutually exclusive
# NICE
#   Allow different separator
#   Allow headline
#   Statistics
# ##############################################################^##############
