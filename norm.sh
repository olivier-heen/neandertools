#!/bin/bash
# ##############################################################v###############
HELP="
Usage   norm.sh <FILE>
FILE    List of cidr, intervals, addresses.
Result  Equivalent list of aligned cidr, merged and deduplicated.
"

FILE="${1}"
[[ ! -f "${FILE}" ]] && echo "${HELP}" && exit 1

(
cidr.py -i	|\
iton.py	|\
tamp.py	|\
sort -un	|\
tamp.py	|\
iton.py	|\
cidr.py	|\
sort -uV
)	<\
"${FILE}"
