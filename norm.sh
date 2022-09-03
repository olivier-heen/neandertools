#!/bin/bash
# ##############################################################v###############
HELP="
Usage   norm.sh <FILE>
FILE    List of cidr, intervals, addresses. Can be stdin.
Result  Equivalent list of aligned cidr, merged and deduplicated.
"

[[ "${1}" == "-h" || "${1}" == "--help" ]] && echo "${HELP}" && exit 1
file=${1:--}

cat "${file}"	|\
cidr.py -i	|\
iton.py	|\
tamp.py	|\
sort -un	|\
tamp.py	|\
iton.py	|\
cidr.py	|\
cidr.py -c	|\
sort -uV
