#!/usr/bin/env python
import sys

try:
    numbers = input('Enter numbers (separate with commas): ')
except:
    print >> sys.stderr, 'Input is not a number!'
    sys.exit(-1)

sum = 0
for currentNumber in numbers:
    sum = sum + currentNumber

print "Sum:", sum, "\n"
