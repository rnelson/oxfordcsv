#!/usr/bin/env python3
from csv import reader
from getopt import getopt
from io import StringIO
from sys import argv, stdin

English = False
Oxford = ',and '

# Handle command line arguments
options, args = getopt(argv[1:], 'E')
for opt, val in options:
    if opt == '-E':
        English = True
        Oxford = ', and'

# Read text or a file from sdtin
csv_text = ''.join(stdin)

# Load that text into a StringIO object, which csv.reader() handles
f = StringIO(csv_text)
f.seek(0)
csv_reader = reader(f, delimiter=',', quotechar='|')

# Oxfordize!
for row in csv_reader:
    if English:
        line = ', '.join(row)
    else:
        line = ','.join(row)

    bits = line.rsplit(',', 1)
    line = Oxford.join(bits)
    print(line)

