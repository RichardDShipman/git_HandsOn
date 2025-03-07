#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Argument parser setup
parser = ArgumentParser(description='Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type=str, required=True, help="Input sequence")
parser.add_argument("-m", "--motif", type=str, required=False, help="Motif")

# Print help if no arguments are provided
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse arguments
args = parser.parse_args()
args.seq = args.seq.upper()  # Convert sequence to uppercase

# Validate and classify sequence
if re.fullmatch(r'^[ACGT]+$', args.seq):  # Only A, C, G, T allowed
    print("The sequence is DNA")
elif re.fullmatch(r'^[ACGU]+$', args.seq):  # Only A, C, G, U allowed
    print("The sequence is RNA")
else:
    print("The sequence is not DNA nor RNA")

# Motif search
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end='')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
