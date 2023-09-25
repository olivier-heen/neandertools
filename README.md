# Neandertools
Old-school tools to ease the manipulation of network data (adresses, ranges, lists).

Most tools are filters and format converters. For instance cidr.py converts cidr to interval and interval to cidr. The lines containing one single correct entry are converted. The other lines are left as is. These tools are made for manual manipulation or simple scripting. Do not use for automated processing with possibly adversarial input.

# Tools
- ``tamp.py`` Convert list of numbers to intervals. And vice-versa.
- ``iton.py`` Convert IPv4 to decimal. And vice-versa. Also works on intervals.
- ``cidr.py`` Convert a cidr network to an address interval. And vice-versa.
- ``turn.py`` Turn a data table into its transpose or into vectors.
- ``norm.sh`` Normalize a mix of cidr intervals and addresses to canonical cidr.
- ``cidrcan.sh`` Find the smallest CIDR range containing an IPv4 address interval.

# Examples
Example: list unique IP addresses from a set of network ranges and intervals.

``cidr.py -i < test/example.01 | iton.py | tamp.py | sort -u | iton.py``

Example: a bash script using the tools to normalize a list of networks.

``norm.sh test/example.01``
