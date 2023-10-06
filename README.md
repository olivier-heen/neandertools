# Neandertools
Old-school and scriptable tools for sets of classless inter-domain routing (CIDR) data.

Imagine you're given a set of IPv4 ranges and intervals and addresses.
You might want to know know how many unique addresses are covered by this set.
You might want to get an equivalent set of normalized and non-overlaping ranges.
Or maybe you just want to answer simple questions about IPv4 networks, such as:
"What is the smallest CIDR range that covers 127.255.255.255 and 128.0.0.0?"

# Tools
- ``tamp.py`` Convert list of numbers to intervals. And vice-versa.
- ``iton.py`` Convert IPv4 to decimal. And vice-versa. Also works on intervals.
- ``cidr.py`` Convert a cidr network to an address interval. And vice-versa.
- ``turn.py`` Turn a data table into its transpose or into vectors.
- ``norm.sh`` Normalize a mix of cidr intervals and addresses to canonical cidr.
- ``cidrcan.sh`` Find the smallest CIDR range containing an IPv4 address interval.

Most neandertools are filters and format converters.
For instance cidr.py converts cidr to interval and interval to cidr.
The lines containing one single correct entry are converted.
The other lines are left as is.
Neandertools are made for manual manipulation and supervised scripting.
Avoid using for fully automated processing with adversarial input data.

# Examples
Example: list unique IP addresses from a set of network ranges and intervals.

``cidr.py -i < test/example.01 | iton.py | tamp.py | sort -u | iton.py``

Example: a bash script using the tools to normalize a list of networks.

``norm.sh test/example.01``
