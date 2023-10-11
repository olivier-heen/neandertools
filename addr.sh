#!/bin/bash
# ##############################################################v###############
help="
Usage   addr.sh <FILE>
FILE    List of cidr, intervals, addresses. Can be stdin.
Result  Equivalent list of unique addresses (can be large).
"

[[ "${1}" == "-h" || "${1}" == "--help" ]] && echo "${help}" && exit 1
file=${1:--}

cat "${file}"	|\
cidr.py -i	|\
iton.py	|\
tamp.py	|\
sort -un	|\
iton.py
