# neandertools
Old-school tools to ease manipulation of network data in scripts.

The tools are filters meant to be piped. They work both ways simultaneosly. The lines containing exactly one correct input are transformed, the other lines rmain unchanged.

Use these tools for manual manipulation and for simple scripting. Do not use for automated processinc with possibly adversarial input.

- ``tamp.py`` Convert successive numbers to intervals. And vice-versa.
- ``iton.py`` Convert IPv4 to decimal. And vice-versa. Also works on intervals.
- ``cidr.py`` Convert cidr network range to addresse interval.  And vice-versa.
- ``turn.py`` Turn a data table into its transpose or into vectors.

Example: list unique IP addresses from a set of network ranges and intervals.

``cidr.py --range < test/example.01 | iton.py | tamp.py | sort -u | iton.py``

Example: normalize a given set of network ranges by correctly aligning the ranges, joinning consecutive ranges and removing doublons.

``cidr.py --range < test/example.02 | iton.py | tamp.py | sort -u | tamp.py | iton.py | cidr.py``
