#!/usr/bin/env python
import StringIO
import csv
import getopt
import sys

English = False
Oxford = ',and '

# Handle command line arguments
options, args = getopt.getopt(sys.argv[1:], 'E')
for opt, val in options:
    if opt == '-E':
        English = True
        Oxford = ', and '

# Read text or a file from sdtin
csv_text = ''.join(sys.stdin)

# Load that text into a StringIO object, which csv.reader() handles
f = StringIO.StringIO(csv_text)
f.seek(0)
csv_reader = csv.reader(f, delimiter=',', quotechar='|')

# Oxfordize!
for row in csv_reader:
    line = ','.join(row)
    bits = line.rsplit(',', 1)
    line = Oxford.join(bits)
    print line
