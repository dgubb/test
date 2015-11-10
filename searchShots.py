#!/usr/bin/env python

import numpy
import sys

input_len=len(sys.argv)
if input_len !=2:
   print('incorrect number of inputs')
   sys.exit(1)

file = sys.argv[1]
data = numpy.loadtxt(fname=file, delimiter=',')

print( data)
